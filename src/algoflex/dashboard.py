import random

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
from algoflex.utils import fmt_secs, time_ago


class Dashboard(Widget):
    show_dashboard = reactive(False)

    # get questions summary by level
    breezy, steady, edgy = set(), set(), set()
    for pid in q.ids:
        question = q.get(pid)
        if question.level == "Breezy":
            breezy.add(pid)
        elif question.level == "Steady":
            steady.add(pid)
        else:
            edgy.add(pid)
    total = len(breezy) + len(steady) + (len(edgy) * 1.5)

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
                    yield Digits("0", id="d_breezy")
                    yield Center(Label(f"of {len(self.breezy)}"))
                with Center(id="steady"):
                    yield Center(Label("Steady"))
                    yield Digits("0", id="d_steady")
                    yield Center(Label(f"of {len(self.steady)}"))
                with Center(id="edgy"):
                    yield Center(Label("Edgy"))
                    yield Digits("0", id="d_edgy")
                    yield Center(Label(f"of {len(self.edgy)}"))
            with Center(id="progress"):
                yield ProgressBar(total=self.total, show_eta=False, id="all")
            with Center():
                yield Static("", id="today")
            with Collapsible(title="Recent Attempts", collapsed=False):
                yield Markdown(id="recent")
            with Collapsible(title="Most Attempts"):
                yield Markdown(id="frequent")
            with Collapsible(title="Speedy Solves"):
                yield Markdown(id="best")
            with Collapsible(title="Slow Solves"):
                yield Markdown(id="worst")

    def watch_show_dashboard(self) -> None:
        ids = ["#d_breezy", "#d_steady", "#d_edgy"]
        if self.show_dashboard:
            breezy, steady, edgy = self.get_complete()
            self.update_digits(ids, [breezy, steady, int(edgy // 1.5)])
            self.update_progress(breezy + steady + edgy)
            self.update_highlight()
            self.update_summary()

    def md_table(self, headers, rows):
        if not rows:
            return "\n\nNo records yet\n\n"
        sep = "|" + "|".join(["---"] * len(headers)) + "|"
        head = "|" + "|".join(headers) + "|"
        body = "\n".join("|" + "|".join(map(str, r)) + "|" for r in rows)
        return f"{head}\n{sep}\n{body}"

    def get_complete(self):
        passed = get_passed_problem_ids()
        breezy = len(self.breezy.intersection(passed))
        steady = len(self.steady.intersection(passed))
        edgy = len(self.edgy.intersection(passed))
        return breezy, steady, edgy * 1.5

    def get_summary(self):
        recent_attempts = get_recent_attempts(n=9)
        most_attempts = get_most_attempted_problems(n=9)

        best_per_problem = get_best_attempts(n=-1)
        cutoff = {"Breezy": 15, "Steady": 25, "Edgy": 40}
        worst_attempts, best_attempts = [], []
        for attempt in best_per_problem:
            level = q.get(attempt["problem_id"]).level
            if attempt["elapsed"] < cutoff[level]:
                best_attempts.append(attempt)
            else:
                worst_attempts.append(attempt)

        languages = {1: "python", 2: "rust"}

        recent = [
            (
                ("✓ " if attempt["passed"] else "x ")
                + q.get(attempt["problem_id"]).title,
                q.get(attempt["problem_id"]).level,
                languages[attempt["lang_id"]],
                fmt_secs(attempt["elapsed"]),
                time_ago(attempt["created_at"]),
            )
            for attempt in recent_attempts
        ]

        frequent = [
            (
                q.get(p["problem_id"]).title,
                q.get(p["problem_id"]).level,
                f"{p['passed_count']}/{p['total_count']}",
            )
            for p in most_attempts
        ]

        fast = [
            (
                "✓ " + q.get(attempt["problem_id"]).title,
                q.get(attempt["problem_id"]).level,
                languages[attempt["lang_id"]],
                fmt_secs(attempt["elapsed"]),
                time_ago(attempt["created_at"]),
            )
            for attempt in best_attempts[:9]
        ]

        forever = [
            (
                "✓ " + q.get(attempt["problem_id"]).title,
                q.get(attempt["problem_id"]).level,
                languages[attempt["lang_id"]],
                fmt_secs(attempt["elapsed"]),
                time_ago(attempt["created_at"]),
            )
            for attempt in worst_attempts[-9:]
        ]

        return recent, frequent, fast, forever

    def get_today_highlight(self):
        passed, total = get_attempts_today()
        comment = self.get_highlight_comment(passed, total)
        return comment, passed, total

    def get_highlight_comment(self, passed, attempts):
        low = ["Solid", "Great", "Cool", "Good"]
        mid = ["Excellent", "Super", "Brill", "Fab", "Legit", "Smooth"]
        high = ["Badass", "Wizard", "Maestro", "Stellar", "Hotshot", "Ninja", "Pro"]

        if passed == 0:
            return "Not bad" if attempts < 6 else "D for dust"
        if passed < 3:
            return random.choice(low)
        elif passed < 5:
            return random.choice(mid)
        elif passed < 9:
            return random.choice(high)
        else:
            return "Ace"

    def update_digits(self, ids, values):
        for id, val in zip(ids, values):
            self.update_digit(id, val)

    def update_digit(self, id, value):
        self.query_one(f"{id}", Digits).update(f"{value}")

    def update_progress(self, value):
        self.query_one(ProgressBar).update(progress=value)

    def update_summary(self) -> None:
        recent, frequent, fast, forever = self.get_summary()
        headers = ["Problem", "Level", "Code", "Time", "When"]
        latest = self.md_table(headers, recent)
        popular = self.md_table(["Problem", "Level", "Passed"], frequent)
        best = self.md_table(headers, fast)
        worst = self.md_table(headers, forever)
        self.query_one("#recent", Markdown).update(latest)
        self.query_one("#frequent", Markdown).update(popular)
        self.query_one("#best", Markdown).update(best)
        self.query_one("#worst", Markdown).update(worst)

    def update_highlight(self):
        comment, passed, total = self.get_today_highlight()
        if not total:
            return
        desc = f"[$primary]{comment}![/] Solved [$primary]{passed}[/] problem{'s' if passed != 1 else ''} in [$primary]{total}[/] attempt{'s' if total != 1 else ''} today."
        today = self.query_one("#today", Static)
        today.update(desc)
        today.border_title = "Today's highlight"
        today.display = True
