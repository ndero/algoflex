from random import choice

from textual.app import ComposeResult
from textual.containers import Center, Horizontal
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import (
    Collapsible,
    Digits,
    Label,
    Markdown,
    ProgressBar,
    Static,
)

from algoflex.db import (
    get_attempts_today,
    get_best_attempts,
    get_most_attempted_problems,
    get_passed_problem_ids,
    get_recent_attempts,
)
from algoflex.questions import questions as q
from algoflex.types import Language, Level, RunStatus
from algoflex.utils import fmt_secs, time_ago


class Dashboard(Widget):
    show_dashboard = reactive(False)

    DEFAULT_CSS = """
    Dashboard {
        overflow-y: auto;
        width: 52vw;
        border-left: vkey $boost;
        border-right: vkey $boost;
        padding: 1 2;
        layer: dashboard;
        align-horizontal: center;
        dock: top;
        offset-x: 100vw;
        transition: offset 100ms;
        &.-visible {
            offset-x: 48vw;
        }

        Bar {
            & > .bar--bar {
                color: $markdown-h1-color;
            }
        }

        #breezy {
            color: green 90%;
        }

        #steady {
            color: orange 70%;
        }

        #edgy {
            color: red 70%;
        }


        #title {
            height: 4;
            color: $markdown-h1-color;
            content-align: center middle;
        }

        #counts {
            height: 7;
        }

        Digits {
            text-align: center;
        }

        #progress {
            height: 3;
        }

        #today {
            display: none;
            border: round white 50%;
            padding: 1 2;
            margin-bottom: 2;
            margin-left: 2;
            margin-right: 2;
            color: white 70%;
        }
    }
    """

    def compose(self) -> ComposeResult:
        with Center(id="dashboard"):
            yield Static("Dashboard", id="title")
            with Horizontal(id="counts"):
                with Center(id="breezy"):
                    yield Center(Label("Breezy"))
                    yield Digits("0", id="breezy_complete")
                    yield Center(Label("of 0", id="breezy_total"))
                with Center(id="steady"):
                    yield Center(Label("Steady"))
                    yield Digits("0", id="steady_complete")
                    yield Center(Label("of 0", id="steady_total"))
                with Center(id="edgy"):
                    yield Center(Label("Edgy"))
                    yield Digits("0", id="edgy_complete")
                    yield Center(Label("of 0", id="edgy_total"))
            with Center(id="progress"):
                yield ProgressBar(show_eta=False, id="all")
            with Center():
                yield Static("", id="today")
            with Collapsible(title="Recent Attempts", collapsed=False):
                yield Markdown(id="recent")
            with Collapsible(title="Most Attempted", collapsed=False):
                yield Markdown(id="frequent")
            with Collapsible(title="Personal Bests"):
                yield Markdown(id="best")

    def on_mount(self) -> None:
        self.breezy_complete = self.query_one("#breezy_complete", Digits)
        self.steady_complete = self.query_one("#steady_complete", Digits)
        self.edgy_complete = self.query_one("#edgy_complete", Digits)
        self.breezy_total = self.query_one("#breezy_total", Label)
        self.steady_total = self.query_one("#steady_total", Label)
        self.edgy_total = self.query_one("#edgy_total", Label)
        self.progress_bar = self.query_one("#all", ProgressBar)
        self.today = self.query_one("#today", Static)
        self.recent_markdown = self.query_one("#recent", Markdown)
        self.frequent_markdown = self.query_one("#frequent", Markdown)
        self.best_markdown = self.query_one("#best", Markdown)

        self.breezy, self.steady, self.edgy = self.problem_levels()
        self.total = (
            len(self.breezy) * Level.BREEZY
            + len(self.steady) * Level.STEADY
            + len(self.edgy) * Level.EDGY
        )

        self.update_dashboard_totals()

    def problem_levels(self) -> tuple[set[int], set[int], set[int]]:
        breezy, steady, edgy = set(), set(), set()
        for pid in q.ids:
            question = q.get(pid)
            if question.level == Level.BREEZY:
                breezy.add(pid)
            elif question.level == Level.STEADY:
                steady.add(pid)
            else:
                edgy.add(pid)

        return breezy, steady, edgy

    def update_dashboard_totals(self) -> None:
        self.breezy_total.update(f"of {len(self.breezy)}")
        self.steady_total.update(f"of {len(self.steady)}")
        self.edgy_total.update(f"of {len(self.edgy)}")
        self.progress_bar.update(total=self.total)

    def watch_show_dashboard(self) -> None:
        if self.show_dashboard:
            breezy, steady, edgy = self.get_complete()
            progress = breezy * Level.BREEZY + steady * Level.STEADY + edgy * Level.EDGY

            self.update_digits(breezy, steady, edgy)
            self.update_progress(progress)
            self.update_highlight()
            self.update_summary()

    def md_table(self, headers, rows) -> str:
        if not rows:
            return "\n\nNo records yet\n\n"
        sep = "|" + "|".join(["---"] * len(headers)) + "|"
        head = "|" + "|".join(headers) + "|"
        body = "\n".join("|" + "|".join(map(str, r)) + "|" for r in rows)
        return f"{head}\n{sep}\n{body}"

    def get_complete(self) -> tuple[int, int, float]:
        passed = get_passed_problem_ids()
        breezy = len(self.breezy.intersection(passed))
        steady = len(self.steady.intersection(passed))
        edgy = len(self.edgy.intersection(passed))
        return breezy, steady, edgy

    def get_summary(self) -> tuple[list, list, list]:
        recent_attempts = get_recent_attempts(n=9)
        most_attempts = get_most_attempted_problems(n=9)
        best_per_problem = get_best_attempts(n=9)

        recent = [
            (
                ("✓ " if RunStatus(attempt["status"]) is RunStatus.PASSED else "x ")
                + q.get(attempt["problem_id"]).title,
                q.get(attempt["problem_id"]).level.label,
                Language(attempt["lang_id"]).label,
                fmt_secs(attempt["elapsed"]),
                time_ago(attempt["created_at"]),
            )
            for attempt in recent_attempts
        ]

        frequent = [
            (
                q.get(p["problem_id"]).title,
                q.get(p["problem_id"]).level.label,
                f"{p['passed_count']}/{p['total_count']}",
            )
            for p in most_attempts
        ]

        fast = [
            (
                "✓ " + q.get(attempt["problem_id"]).title,
                q.get(attempt["problem_id"]).level.label,
                Language(attempt["lang_id"]).label,
                fmt_secs(attempt["elapsed"]),
                time_ago(attempt["created_at"]),
            )
            for attempt in best_per_problem
        ]

        return recent, frequent, fast

    def get_today_highlight(self) -> tuple[str, int, int]:
        passed, total = get_attempts_today()
        comment = self.get_highlight_comment(passed, total)
        return comment, passed, total

    def get_highlight_comment(self, passed: int, attempts: int) -> str:
        if passed == 0:
            return "Not bad" if attempts < 6 else "D for dust"
        if passed < 3:
            return choice(["Solid", "Great", "Cool", "Good"])
        if passed < 5:
            return choice(["Excellent", "Super", "Brill", "Fab", "Legit", "Smooth"])
        if passed < 9:
            return choice(["Wizard", "Maestro", "Hotshot", "Pro"])
        return "Ace"

    def update_digits(self, breezy, steady, edgy) -> None:
        self.breezy_complete.update(f"{breezy}")
        self.steady_complete.update(f"{steady}")
        self.edgy_complete.update(f"{edgy}")

    def update_progress(self, value) -> None:
        self.progress_bar.update(progress=value)

    def update_summary(self) -> None:
        recent, frequent, fast = self.get_summary()
        headers = ["Problem", "Level", "Language", "Duration", "When"]
        latest = self.md_table(headers, recent)
        popular = self.md_table(["Problem", "Level", "Passed"], frequent)
        best = self.md_table(headers, fast)
        self.recent_markdown.update(latest)
        self.frequent_markdown.update(popular)
        self.best_markdown.update(best)

    def update_highlight(self) -> None:
        comment, passed, total = self.get_today_highlight()
        if not total:
            return
        desc = f"[$primary]{comment}![/] Solved [$primary]{passed}[/] problem{'s' if passed != 1 else ''} in [$primary]{total}[/] attempt{'s' if total != 1 else ''} today."
        self.today.update(desc)
        self.today.border_title = "Today's highlight"
        self.today.display = True
