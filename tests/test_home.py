from typing import ClassVar

import pytest
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Markdown, Static

from algoflex import home
from algoflex.home import HomeScreen, StatScreen
from algoflex.types import Language, Level, RunStatus


# Test doubles
class FakeQuestion:
    def __init__(
        self,
        id: int,
        title: str,
        level: Level,
        markdown: str,
        languages: list[Language] | None = None,
    ) -> None:
        self.id = id
        self.title = title
        self.level = level
        self.markdown = markdown
        self.languages = (
            languages if languages is not None else [Language.PYTHON, Language.RUST]
        )


class FakeQuestions:
    ids: ClassVar = [1, 2, 3]

    def __init__(self) -> None:
        self._questions = {
            1: FakeQuestion(
                1,
                "Two Sum",
                Level.BREEZY,
                "# Two Sum\n\nFind two numbers.",
                [Language.PYTHON, Language.RUST],
            ),
            2: FakeQuestion(
                2,
                "Binary Search",
                Level.STEADY,
                "# Binary Search\n\nSearch a sorted array.",
                [Language.PYTHON],
            ),
            3: FakeQuestion(
                3,
                "Trap Rain Water",
                Level.EDGY,
                "# Trap Rain Water\n\nCalculate trapped water.",
                [Language.RUST],
            ),
        }

    def get(self, problem_id: int) -> FakeQuestion:
        return self._questions[problem_id]


class FakeAttemptScreen(Screen):
    def __init__(self, question, language: Language, draft) -> None:
        super().__init__()
        self.question = question
        self.language = language
        self.draft = draft


class FakeSearchScreen(Screen):
    pass


class HomeTestApp(HomeScreen):
    """Convenience subclass used only to make the test intent explicit."""


class AppForStats(App):
    """Minimal host app for a standalone StatScreen."""

    def compose(self) -> ComposeResult:
        yield StatScreen()


# Fixtures and helpers
@pytest.fixture
def fake_questions(monkeypatch):
    questions = FakeQuestions()
    monkeypatch.setattr(home, "questions", questions)
    return questions


@pytest.fixture
def deterministic_shuffle(monkeypatch):
    monkeypatch.setattr(home, "shuffle", lambda values: None)


@pytest.fixture
def home_app(fake_questions, deterministic_shuffle):
    return HomeTestApp()


def stub_problem_sources(
    monkeypatch,
    *,
    pass_ratio=(0, 0),
    recent=None,
    best=None,
    fmt_secs=None,
    time_ago=None,
):
    monkeypatch.setattr(home, "get_problem_pass_ratio", lambda problem_id: pass_ratio)
    monkeypatch.setattr(
        home, "get_recent_attempts", lambda *, n, problem_id: recent or []
    )
    monkeypatch.setattr(home, "get_best_attempts", lambda *, n, problem_id: best or [])

    if fmt_secs is not None:
        monkeypatch.setattr(home, "fmt_secs", fmt_secs)
    if time_ago is not None:
        monkeypatch.setattr(home, "time_ago", time_ago)


def stub_attempt_action(monkeypatch, *, recent=None, draft=None):
    """Stub the collaborators used by HomeScreen.action_attempt.

    Returns a dict that records the keyword arguments that were passed to
    get_draft, so tests can assert on problem_id/lang_id selection.
    """
    captured: dict = {}

    def fake_get_draft(*, problem_id, lang_id):
        captured["problem_id"] = problem_id
        captured["lang_id"] = lang_id
        return draft

    monkeypatch.setattr(home, "AttemptScreen", FakeAttemptScreen)
    monkeypatch.setattr(
        home, "get_recent_attempts", lambda *, n, problem_id=None: recent or []
    )
    monkeypatch.setattr(home, "get_draft", fake_get_draft)
    return captured


def capture_search_callback(monkeypatch, app):
    """Replace push_screen and expose the on_close callback the app passes.

    Returns a dict with "screen" and "on_close" keys populated once
    action_search has been called.
    """
    captured: dict = {}

    def fake_push_screen(screen, on_close):
        captured["screen"] = screen
        captured["on_close"] = on_close

    monkeypatch.setattr(home, "SearchScreen", FakeSearchScreen)
    monkeypatch.setattr(app, "push_screen", fake_push_screen)
    return captured


# StatScreen
class TestStatScreen:
    @pytest.mark.asyncio
    async def test_composes_expected_widgets(self):
        app = AppForStats()

        async with app.run_test():
            assert app.query_one("#passed", Static)
            assert app.query_one("#last", Static)
            assert app.query_one("#best", Static)
            assert app.query_one("#level", Static)

    @pytest.mark.asyncio
    async def test_has_expected_initial_values(self):
        app = AppForStats()

        async with app.run_test():
            assert str(app.query_one("#passed", Static).content) == "0/0"
            assert str(app.query_one("#last", Static).content) == "..."
            assert str(app.query_one("#best", Static).content) == "..."
            assert str(app.query_one("#level", Static).content) == "..."


# HomeScreen initial state
class TestHomeInitialState:
    @pytest.mark.asyncio
    async def test_composes_expected_widgets(self, home_app):
        async with home_app.run_test():
            assert home_app.query_one(Footer)
            assert home_app.query_one("#title", Static)
            assert home_app.query_one("#passed", Static)
            assert home_app.query_one("#last", Static)
            assert home_app.query_one("#best", Static)
            assert home_app.query_one("#level", Static)
            assert home_app.query_one(Markdown)

    @pytest.mark.asyncio
    async def test_initializes_problems(self, home_app):
        async with home_app.run_test():
            assert home_app.problems == [1, 2, 3]
            assert home_app.problems_count == 3
            assert home_app.question.id == 1

    @pytest.mark.asyncio
    async def test_starts_at_first_problem(self, home_app):
        async with home_app.run_test():
            assert home_app.index == 0
            assert home_app.question.id == 1

    @pytest.mark.asyncio
    async def test_starts_with_dashboard_hidden(self, home_app):
        async with home_app.run_test():
            assert home_app.show_dashboard is False


# Problem details
class TestProblemDetails:
    @pytest.mark.asyncio
    async def test_returns_problem_without_attempts(self, home_app, monkeypatch):
        stub_problem_sources(monkeypatch)

        async with home_app.run_test():
            assert home_app.get_problem_details() == (
                "# Two Sum\n\nFind two numbers.",
                Level.BREEZY,
                0,
                0,
                "...",
                "...",
            )

    @pytest.mark.asyncio
    async def test_includes_attempt_statistics(self, home_app, monkeypatch):
        stub_problem_sources(
            monkeypatch,
            pass_ratio=(3, 5),
            recent=[{"status": RunStatus.PASSED, "created_at": 1000.0}],
            best=[{"elapsed": 125.0}],
            fmt_secs=lambda elapsed: f"{elapsed} seconds",
            time_ago=lambda timestamp: f"{timestamp} ago",
        )

        async with home_app.run_test():
            assert home_app.get_problem_details() == (
                "# Two Sum\n\nFind two numbers.",
                Level.BREEZY,
                3,
                5,
                f"{RunStatus.PASSED.icon} 1000.0 ago",
                "125.0 seconds",
            )

    @pytest.mark.asyncio
    async def test_uses_failed_status_icon(self, home_app, monkeypatch):
        stub_problem_sources(
            monkeypatch,
            pass_ratio=(0, 1),
            recent=[{"status": RunStatus.FAILED, "created_at": 1000.0}],
            time_ago=lambda timestamp: "1 min ago",
        )

        async with home_app.run_test():
            details = home_app.get_problem_details()

            assert details[4] == f"{RunStatus.FAILED.icon} 1 min ago"


# Problem rendering
class TestProblemRendering:
    @pytest.mark.asyncio
    async def test_update_problem_view(self, home_app, monkeypatch):
        monkeypatch.setattr(
            home_app,
            "get_problem_details",
            lambda: (
                "# Two Sum",
                Level.BREEZY,
                2,
                4,
                "✓ 1 min ago",
                "5 mins",
            ),
        )

        async with home_app.run_test():
            home_app.update_problem_view()

            assert str(home_app.query_one(Markdown).source) == "# Two Sum"
            assert str(home_app.query_one("#passed", Static).content) == "2/4"
            assert str(home_app.query_one("#last", Static).content) == "✓ 1 min ago"
            assert str(home_app.query_one("#best", Static).content) == "5 mins"
            assert "Breezy" in str(home_app.query_one("#level", Static).content)


# Navigation
class TestNavigation:
    @pytest.mark.asyncio
    async def test_next_moves_to_next_problem(self, home_app):
        async with home_app.run_test():
            home_app.action_next()

            assert home_app.index == 1
            assert home_app.question.id == 2

    @pytest.mark.asyncio
    async def test_next_does_not_move_past_last_problem(self, home_app):
        async with home_app.run_test():
            home_app.index = home_app.problems_count - 1

            home_app.action_next()

            assert home_app.index == home_app.problems_count - 1
            assert home_app.question.id == 3

    @pytest.mark.asyncio
    async def test_previous_moves_to_previous_problem(self, home_app):
        async with home_app.run_test():
            home_app.index = 2

            home_app.action_previous()

            assert home_app.index == 1
            assert home_app.question.id == 2

    @pytest.mark.asyncio
    async def test_previous_does_not_move_before_first_problem(self, home_app):
        async with home_app.run_test():
            home_app.action_previous()

            assert home_app.index == 0
            assert home_app.question.id == 1

    @pytest.mark.asyncio
    async def test_next_hides_dashboard(self, home_app):
        async with home_app.run_test():
            home_app.show_dashboard = True

            home_app.action_next()

            assert home_app.show_dashboard is False

    @pytest.mark.asyncio
    async def test_previous_hides_dashboard(self, home_app):
        async with home_app.run_test():
            home_app.show_dashboard = True

            home_app.action_previous()

            assert home_app.show_dashboard is False


# Dashboard visibility
class TestDashboardVisibility:
    @pytest.mark.asyncio
    async def test_action_toggles_visibility(self, home_app):
        async with home_app.run_test():
            assert home_app.show_dashboard is False

            home_app.action_dashboard()
            assert home_app.show_dashboard is True

            home_app.action_dashboard()
            assert home_app.show_dashboard is False

    @pytest.mark.asyncio
    async def test_show_dashboard_updates_dashboard_class(self, home_app):
        async with home_app.run_test():
            dashboard = home_app.query_one(home.Dashboard)

            assert not dashboard.has_class("-visible")

            home_app.show_dashboard = True
            assert dashboard.has_class("-visible")

            home_app.show_dashboard = False
            assert not dashboard.has_class("-visible")


# Attempt action
class TestActionAttempt:
    @pytest.mark.asyncio
    async def test_defaults_to_python_when_no_recent_attempt(
        self, home_app, monkeypatch
    ):
        captured = stub_attempt_action(monkeypatch)

        async with home_app.run_test() as pilot:
            home_app.action_attempt()
            await pilot.pause()

            assert captured == {
                "problem_id": 1,
                "lang_id": Language.PYTHON,
            }

            assert isinstance(home_app.screen, FakeAttemptScreen)
            assert home_app.screen.question is home_app.question
            assert home_app.screen.language is Language.PYTHON
            assert home_app.screen.draft is None

    @pytest.mark.asyncio
    async def test_uses_supported_recent_language(self, home_app, monkeypatch):
        stub_attempt_action(
            monkeypatch,
            recent=[
                {
                    "created_at": 1_000.0,
                    "lang_id": Language.RUST,
                    "status": RunStatus.PASSED,
                }
            ],
            draft="draft",
        )

        async with home_app.run_test() as pilot:
            home_app.action_attempt()
            await pilot.pause()

            assert isinstance(home_app.screen, FakeAttemptScreen)
            assert home_app.screen.language is Language.RUST
            assert home_app.screen.draft == "draft"

    @pytest.mark.asyncio
    async def test_falls_back_to_first_supported_language_when_recent_language_unsupported(
        self, home_app, monkeypatch
    ):
        captured = stub_attempt_action(
            monkeypatch,
            recent=[
                {
                    "created_at": 1_000.0,
                    "lang_id": Language.RUST,
                    "status": RunStatus.PASSED,
                }
            ],
        )

        async with home_app.run_test() as pilot:
            home_app.index = 1  # question 2 only supports python
            await pilot.pause()

            home_app.action_attempt()
            await pilot.pause()

            assert isinstance(home_app.screen, FakeAttemptScreen)
            assert home_app.screen.question.languages == [Language.PYTHON]
            assert home_app.screen.language is Language.PYTHON
            assert captured == {
                "problem_id": 2,
                "lang_id": Language.PYTHON,
            }

    @pytest.mark.asyncio
    async def test_hides_dashboard(self, home_app, monkeypatch):
        stub_attempt_action(monkeypatch)

        async with home_app.run_test() as pilot:
            home_app.show_dashboard = True

            home_app.action_attempt()
            await pilot.pause()

            assert home_app.show_dashboard is False

    @pytest.mark.asyncio
    async def test_passes_current_question(self, home_app, monkeypatch):
        stub_attempt_action(monkeypatch)

        async with home_app.run_test() as pilot:
            home_app.action_attempt()
            await pilot.pause()

            assert isinstance(home_app.screen, FakeAttemptScreen)
            assert home_app.screen.question.id == 1
            assert home_app.screen.question.title == "Two Sum"


# Search action
class TestActionSearch:
    @pytest.mark.asyncio
    async def test_hides_dashboard(self, home_app, monkeypatch):
        monkeypatch.setattr(home, "SearchScreen", FakeSearchScreen)

        async with home_app.run_test() as pilot:
            home_app.show_dashboard = True
            home_app.action_search()
            await pilot.pause()

            assert home_app.show_dashboard is False
            assert isinstance(home_app.screen, FakeSearchScreen)

    @pytest.mark.asyncio
    async def test_callback_selects_existing_problem(self, home_app, monkeypatch):
        captured = capture_search_callback(monkeypatch, home_app)

        async with home_app.run_test():
            home_app.action_search()

            assert captured["on_close"] is not None

            captured["on_close"](3)

            assert home_app.index == 2
            assert home_app.question.id == 3

    @pytest.mark.asyncio
    async def test_callback_ignores_unknown_problem(self, home_app, monkeypatch):
        captured = capture_search_callback(monkeypatch, home_app)

        async with home_app.run_test():
            home_app.index = 1

            home_app.action_search()

            assert captured["on_close"] is not None

            captured["on_close"](999)

            assert home_app.index == 1

    @pytest.mark.asyncio
    async def test_callback_ignores_cancel(self, home_app, monkeypatch):
        captured = capture_search_callback(monkeypatch, home_app)

        async with home_app.run_test():
            home_app.index = 1

            home_app.action_search()

            assert captured["on_close"] is not None

            captured["on_close"](None)

            assert home_app.index == 1


# Action availability
class TestActionAvailability:
    @pytest.mark.parametrize(
        ("action", "expected"),
        [
            ("attempt", True),
            ("next", True),
            ("previous", None),
            ("search", True),
            ("dashboard", True),
        ],
    )
    @pytest.mark.asyncio
    async def test_at_first_problem(self, home_app, action, expected):
        async with home_app.run_test():
            home_app.index = 0

            assert home_app.check_action(action, []) is expected

    @pytest.mark.parametrize(
        ("action", "expected"),
        [
            ("attempt", True),
            ("next", None),
            ("previous", True),
            ("search", True),
            ("dashboard", True),
        ],
    )
    @pytest.mark.asyncio
    async def test_at_last_problem(self, home_app, action, expected):
        async with home_app.run_test():
            home_app.index = home_app.problems_count - 1

            assert home_app.check_action(action, []) is expected

    @pytest.mark.asyncio
    async def test_at_intermediate_problem(self, home_app):
        async with home_app.run_test():
            home_app.index = 1

            assert home_app.check_action("attempt", []) is True
            assert home_app.check_action("next", []) is True
            assert home_app.check_action("previous", []) is True
            assert home_app.check_action("search", []) is True
            assert home_app.check_action("dashboard", []) is True

    @pytest.mark.asyncio
    async def test_hides_home_actions_on_non_default_screen(self, home_app):
        async with home_app.run_test():
            home_app.push_screen(FakeSearchScreen())

            assert home_app.check_action("attempt", []) is False
            assert home_app.check_action("next", []) is False
            assert home_app.check_action("previous", []) is False
            assert home_app.check_action("search", []) is False
            assert home_app.check_action("dashboard", []) is False
