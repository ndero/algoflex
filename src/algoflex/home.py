from random import shuffle
from typing import ClassVar

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.reactive import reactive
from textual.widgets import Footer, Markdown, Static

from algoflex.attempt import AttemptScreen
from algoflex.custom_widgets import Problem, Title
from algoflex.dashboard import Dashboard
from algoflex.db import (
    get_best_attempts,
    get_draft,
    get_problem_pass_ratio,
    get_recent_attempts,
)
from algoflex.questions import questions
from algoflex.search import SearchScreen
from algoflex.types import Language
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

    LEVEL_COLORS: ClassVar[dict[str, str]] = {
        "Breezy": "green 90%",
        "Steady": "orange 70%",
        "Edgy": "red 70%",
    }

    index: reactive[int] = reactive(0, bindings=True)
    show_dashboard: reactive[bool] = reactive(False)

    @property
    def problem_id(self) -> int:
        return self.problems[self.index]

    @property
    def problems_count(self) -> int:
        return len(self.problems)

    def compose(self) -> ComposeResult:
        yield Title()
        with VerticalScroll():
            yield Dashboard().data_bind(HomeScreen.show_dashboard)
            yield Problem("")
            yield StatScreen()
        yield Footer()

    def on_mount(self) -> None:
        self.problems = list(questions.ids)
        shuffle(self.problems)

        self.passed = self.query_one("#passed", Static)
        self.last = self.query_one("#last", Static)
        self.best = self.query_one("#best", Static)
        self.level = self.query_one("#level", Static)
        self.problem = self.query_one(Problem)
        self.markdown = self.problem.query_one(Markdown)

    def watch_index(self) -> None:
        self.update_problem_view()

    def get_problem_details(self) -> tuple:
        p = questions.get(self.problem_id)
        markdown, level = p.markdown, p.level
        passed, total = get_problem_pass_ratio(self.problem_id)
        last_attempts = get_recent_attempts(n=1, problem_id=self.problem_id)
        best_attempts = get_best_attempts(n=1, problem_id=self.problem_id)
        best = fmt_secs(best_attempts[0]["elapsed"]) if best_attempts else "..."

        last = "..."
        if last_attempts:
            row = last_attempts[0]
            last = ("🟢 " if row["passed"] else "🔴 ") + time_ago(row["created_at"])

        return markdown, level, passed, total, last, best

    def update_problem_view(self) -> None:
        markdown, level, passed, total, last, best = self.get_problem_details()
        self.markdown.update(markdown)
        self.problem.scroll_home()
        self.level.update(f"[{self.LEVEL_COLORS.get(level, '$primary')}]{level}[/]")

        self.passed.update(f"{passed!s}/{total!s}")
        self.last.update(f"{last}")
        self.best.update(f"{best}")

    def watch_show_dashboard(self, show_dashboard) -> None:
        dashboard = self.query_one(Dashboard)
        dashboard.set_class(show_dashboard, "-visible")

    def action_attempt(self) -> None:
        if self.show_dashboard:
            self.show_dashboard = False

        def update(_id):
            self.update_problem_view()

        recent = get_recent_attempts(n=1)
        language = Language(recent[0]["lang_id"]) if recent else Language.PYTHON
        draft = get_draft(problem_id=self.problem_id, lang_id=language)
        self.push_screen(AttemptScreen(self.problem_id, language, draft), update)

    def action_next(self) -> None:
        if self.show_dashboard:
            self.show_dashboard = False
        if self.index + 1 < self.problems_count:
            self.index += 1

    def action_previous(self) -> None:
        if self.show_dashboard:
            self.show_dashboard = False
        if self.index > 0:
            self.index -= 1

    def action_search(self) -> None:
        def on_close(result):
            if result is None:
                return
            if result in self.problems:
                self.index = self.problems.index(result)

        if self.show_dashboard:
            self.show_dashboard = False
        self.push_screen(SearchScreen(), on_close)

    def action_dashboard(self) -> None:
        self.show_dashboard = not self.show_dashboard

    def check_action(self, action, parameters) -> bool | None:
        """
        Returns:
            True  - show footer key active
            False - hide footer key
            None  - show footer key disabled
        """
        if self.screen.id != "_default" and action in {
            "attempt",
            "next",
            "previous",
            "search",
            "dashboard",
        }:
            return False
        if self.index == self.problems_count - 1 and action == "next":
            return
        if self.index == 0 and action == "previous":
            return
        return True
