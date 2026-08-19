from random import shuffle
from typing import ClassVar

from textual.app import App
from textual.binding import Binding
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.reactive import reactive
from textual.widgets import Footer, Markdown, Static

from algoflex.attempt import AttemptScreen
from algoflex.custom_widgets import Problem, Title
from algoflex.dashboard import Dashboard
from algoflex.db import get_best_attempts, get_problem_pass_ratio, get_recent_attempts
from algoflex.questions import questions
from algoflex.search import SearchScreen
from algoflex.utils import fmt_secs, time_ago


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
            color: $primary;
        }
    }
    """

    def compose(self):
        with Horizontal():
            with Vertical():
                yield Static("[b]Passed[/]")
                yield Static("0/0", id="passed")
            with Vertical():
                yield Static("[b]Last attempt[/]")
                yield Static("...", id="last")
            with Vertical():
                yield Static("[b]Best attempt[/]")
                yield Static("...", id="best")
            with Vertical():
                yield Static("[b]Level[/]")
                yield Static("...", id="level")


class HomeScreen(App):
    BINDINGS: ClassVar[list[Binding]] = [
        Binding("a", "attempt", "attempt", tooltip="Attempt this question"),
        Binding("p", "previous", "previous", tooltip="Previous question"),
        Binding("n", "next", "next", tooltip="Next question"),
        Binding("s", "search", "search"),
        Binding("d", "dashboard", "dashboard", tooltip="Show dashboard"),
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

    Screen {
        layers: dashboard;
    }
    """
    PROBLEMS: ClassVar = list(questions.ids)
    PROBLEMS_COUNT = len(PROBLEMS)

    index = reactive(0, bindings=True)
    show_dashboard: reactive[bool] = reactive(False)

    @property
    def problem_id(self):
        return self.PROBLEMS[self.index]

    def compose(self):
        yield Title()
        with VerticalScroll():
            yield Dashboard().data_bind(HomeScreen.show_dashboard)
            yield Problem("")
            yield StatScreen()
        yield Footer()

    def on_mount(self):
        shuffle(self.PROBLEMS)

    def watch_index(self) -> None:
        self.update_problem_view()

    def update_problem_view(self):
        p = questions.get(self.problem_id)
        markdown, level = p.markdown, p.level

        problem_widget = self.query_one(Problem)
        problem_widget.query_one(Markdown).update(markdown)
        problem_widget.scroll_home()
        self.update_level(level)

        passed, total = get_problem_pass_ratio(self.problem_id)
        last_attempts = get_recent_attempts(n=1, problem_id=self.problem_id)
        best_attempts = get_best_attempts(n=1, problem_id=self.problem_id)
        best = fmt_secs(best_attempts[0]["elapsed"]) if best_attempts else "..."

        last = "..."
        if last_attempts:
            row = last_attempts[0]
            last = ("🟢 " if row["passed"] else "🔴 ") + time_ago(row["created_at"])

        self.query_one("#passed", Static).update(f"{passed!s}/{total!s}")
        self.query_one("#last", Static).update(f"{last}")
        self.query_one("#best", Static).update(f"{best}")

    def update_level(self, level):
        target = self.query_one("#level", Static)
        colors = {"Breezy": "green 90%", "Steady": "orange 70%", "Edgy": "red 70%"}
        target.update(f"[{colors.get(level, '$primary')}]{level}[/]")

    def watch_show_dashboard(self, show_dashboard) -> None:
        dashboard = self.query_one(Dashboard)
        dashboard.set_class(show_dashboard, "-visible")

    def action_attempt(self):
        if self.show_dashboard:
            self.show_dashboard = False

        def update(_id):
            self.update_problem_view()

        self.push_screen(AttemptScreen(self.problem_id), update)

    def action_next(self):
        if self.show_dashboard:
            self.show_dashboard = False
        if self.index + 1 < self.PROBLEMS_COUNT:
            self.index += 1

    def action_previous(self):
        if self.show_dashboard:
            self.show_dashboard = False
        if self.index > 0:
            self.index -= 1

    def action_search(self):
        def on_close(result):
            if result is None:
                return
            if result in self.PROBLEMS:
                self.index = self.PROBLEMS.index(result)

        if self.show_dashboard:
            self.show_dashboard = False
        self.push_screen(SearchScreen(), on_close)

    def action_dashboard(self):
        self.show_dashboard = not self.show_dashboard

    def check_action(self, action, parameters):
        if self.screen.id != "_default" and (
            action == "attempt"
            or action == "next"
            or action == "previous"
            or action == "search"
            or action == "dashboard"
        ):
            return False
        if self.index == self.PROBLEMS_COUNT - 1 and action == "next":
            return
        if self.index == 0 and action == "previous":
            return
        return True
