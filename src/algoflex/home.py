from textual.app import App
from textual.screen import Screen
from textual.containers import Horizontal, Vertical, VerticalScroll, HorizontalScroll
from textual.widgets import Footer, Markdown, Static
from textual.binding import Binding
from textual.reactive import Reactive
from algoflex.questions import questions
from algoflex.attempt import AttemptScreen
from algoflex.custom_widgets import Title, Problem
from algoflex.db import get_db
from random import shuffle
from tinydb import Query
import time

KV = Query()


class StatScreen(Vertical):
    DEFAULT_CSS = """
    Horizontal {
        Vertical {
            background: $boost;
            padding: 1;
            margin: 1 0;
        }
        #passed, #last, #best, #level {
            padding-top: 1;
        }
    }
    """

    def compose(self):
        with Horizontal():
            with Vertical():
                yield Static("[b]Passed[/]")
                yield Static("...", id="passed")
            with Vertical():
                yield Static("[b]Best time[/]")
                yield Static("...", id="best")
            with Vertical():
                yield Static("[b]Last attempt[/]")
                yield Static("...", id="last")
            with Vertical():
                yield Static("[b]Level[/]")
                yield Static("...", id="level")


class HomeScreen(App):
    BINDINGS = [
        Binding("a", "attempt", "attempt", tooltip="Attempt this question"),
        Binding("n", "next", "next", tooltip="Next question"),
        Binding("p", "previous", "previous", tooltip="Previous question"),
    ]
    DEFAULT_CSS = """
    HomeScreen {
        Problem {
            &>*{ max-width: 100; }
            align: center middle;
            margin-top: 1;
        }
        StatScreen {
            height: 7;
            &>* {max-width: 100; }
            align: center middle;
        }
    }
    """
    problem_id = Reactive(0, always_update=True)
    index = Reactive(0, bindings=True)
    PROBLEMS_COUNT = len(questions.keys())
    PROBLEMS = [i for i in range(PROBLEMS_COUNT)]

    def compose(self):
        problem = questions.get(id, {}).get("markdown", "")
        yield Title()
        with VerticalScroll():
            yield Problem(problem)
            yield StatScreen()
        yield Footer()

    def on_mount(self):
        shuffle(self.PROBLEMS)
        self.problem_id = self.PROBLEMS[self.index]

    def hrs_mins_secs(self, tm):
        if isinstance(tm, str):
            return tm
        mins, secs = divmod(tm, 60)
        hrs, mins = divmod(mins, 60)
        if hrs > 23:
            return self.time_ago(tm)
        return f"{hrs:02,.0f}:{mins:02.0f}:{secs:02.0f}"

    def time_ago(self, tm):
        if isinstance(tm, str):
            return tm
        secs = int(time.time() - tm)
        mn, hr, day, week, month, year = (
            60,
            3600,
            86_400,
            604_800,
            2_592_000,
            31_104_000,
        )
        if secs < mn:
            v = secs // 1
            return f"{v} second{'s' if v > 1 else ''}"
        if secs < hr:
            v = secs // mn
            return f"{v} minute{'s' if v > 1 else ''}"
        if secs < day:
            v = secs // hr
            return f"{v} hour{'s' if v > 1 else ''}"
        if secs < week:
            v = secs // day
            return f"{v} day{'s' if v > 1 else ''}"
        if secs < month:
            v = secs // week
            return f"{v} week{'s' if v > 1 else ''}"
        if secs < year:
            v = secs // month
            return f"{v} month{'s' if v > 1 else ''}"
        v = secs // year
        return f"{v} year{'s' if v > 1 else ''}"

    def watch_problem_id(self, id):
        stats = get_db()
        s = stats.get(KV.problem_id == id) or {}
        p = questions.get(id, {})
        problem, level = p.get("markdown", ""), p.get("level", "Breezy")
        passed, attempts, last_at, best_elapsed = (
            s.get("passed", "0"),
            s.get("attempts", "0"),
            self.time_ago(s.get("last_at", "...")),
            self.hrs_mins_secs(s.get("best_elapsed", "...")),
        )
        problem_widget = self.query_one(Problem)
        problem_widget.query_one(Markdown).update(markdown=problem)
        problem_widget.scroll_home()
        s_widget = self.query_one(StatScreen)
        s_widget.query_one("#passed").update(
            f"[$primary]{str(passed)}/{str(attempts)}[/]"
        )
        last, best = s_widget.query_one("#last"), s_widget.query_one("#best")
        last.update(f"[$primary]{last_at} {'ago' if last_at != '...' else ''}[/]")
        best.update(f"[$primary]{best_elapsed}[/]")
        s_widget.query_one("#level").update(f"[$primary]{level}[/]")

    def action_attempt(self):
        def update(_id):
            self.problem_id = self.PROBLEMS[self.index]

        self.push_screen(AttemptScreen(self.problem_id), update)

    def action_next(self):
        if self.index + 1 < self.PROBLEMS_COUNT:
            self.index += 1
        self.problem_id = self.PROBLEMS[self.index]

    def action_previous(self):
        if self.index > 0:
            self.index -= 1
        self.problem_id = self.PROBLEMS[self.index]

    def check_action(self, action, parameters):
        if not self.screen.id == "_default":
            if action == "attempt" or action == "next" or action == "previous":
                return False
        if self.index == self.PROBLEMS_COUNT - 1 and action == "next":
            return
        if self.index == 0 and action == "previous":
            return
        return True
