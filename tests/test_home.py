from typing import ClassVar

import pytest
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Markdown, Static

from algoflex import home
from algoflex.home import HomeScreen, StatScreen
from algoflex.types import Language, Level, RunStatus


class FakeQuestion:
    def __init__(
        self,
        title: str,
        level: Level,
        markdown: str,
    ) -> None:
        self.title = title
        self.level = level
        self.markdown = markdown


class FakeQuestions:
    ids: ClassVar = [1, 2, 3]

    def __init__(self) -> None:
        self._questions = {
            1: FakeQuestion(
                "Two Sum",
                Level.BREEZY,
                "# Two Sum\n\nFind two numbers.",
            ),
            2: FakeQuestion(
                "Binary Search",
                Level.STEADY,
                "# Binary Search\n\nSearch a sorted array.",
            ),
            3: FakeQuestion(
                "Trap Rain Water",
                Level.EDGY,
                "# Trap Rain Water\n\nCalculate trapped water.",
            ),
        }

    def get(self, problem_id: int) -> FakeQuestion:
        return self._questions[problem_id]


class FakeAttemptScreen(Screen):
    def __init__(
        self,
        problem_id: int,
        language: Language,
        draft,
    ) -> None:
        super().__init__()
        self.problem_id = problem_id
        self.language = language
        self.draft = draft


class FakeSearchScreen(Screen):
    pass


class HomeTestApp(HomeScreen):
    """Convenience subclass used only to make the test intent explicit."""


@pytest.fixture
def fake_questions(monkeypatch):
    questions = FakeQuestions()
    monkeypatch.setattr(home, "questions", questions)
    return questions


@pytest.fixture
def deterministic_shuffle(monkeypatch):
    monkeypatch.setattr(
        home,
        "shuffle",
        lambda values: None,
    )


@pytest.fixture
def home_app(fake_questions, deterministic_shuffle):
    return HomeTestApp()


# StatScreen
@pytest.mark.asyncio
async def test_stat_screen_composes_expected_widgets():
    class AppForStats(App):
        def compose(self) -> ComposeResult:
            yield StatScreen()

    app = AppForStats()

    async with app.run_test():
        assert app.query_one("#passed", Static)
        assert app.query_one("#last", Static)
        assert app.query_one("#best", Static)
        assert app.query_one("#level", Static)


@pytest.mark.asyncio
async def test_stat_screen_has_expected_initial_values():
    class AppForStats(App):
        def compose(self) -> ComposeResult:
            yield StatScreen()

    app = AppForStats()

    async with app.run_test():
        assert str(app.query_one("#passed", Static).content) == "0/0"
        assert str(app.query_one("#last", Static).content) == "..."
        assert str(app.query_one("#best", Static).content) == "..."
        assert str(app.query_one("#level", Static).content) == "..."


# HomeScreen composition / initial state
@pytest.mark.asyncio
async def test_home_composes_expected_widgets(home_app):
    async with home_app.run_test():
        assert home_app.query_one(Footer)
        assert home_app.query_one("#title", Static)
        assert home_app.query_one("#passed", Static)
        assert home_app.query_one("#last", Static)
        assert home_app.query_one("#best", Static)
        assert home_app.query_one("#level", Static)
        assert home_app.query_one(Markdown)


@pytest.mark.asyncio
async def test_home_initializes_problems(home_app, fake_questions):
    async with home_app.run_test():
        assert home_app.problems == [1, 2, 3]
        assert home_app.problems_count == 3
        assert home_app.problem_id == 1


@pytest.mark.asyncio
async def test_home_starts_with_dashboard_hidden(home_app):
    async with home_app.run_test():
        assert home_app.show_dashboard is False


@pytest.mark.asyncio
async def test_home_starts_at_first_problem(home_app):
    async with home_app.run_test():
        assert home_app.index == 0
        assert home_app.problem_id == 1


# Problem details
@pytest.mark.asyncio
async def test_get_problem_details_returns_problem_without_attempts(
    home_app,
    fake_questions,
    monkeypatch,
):
    monkeypatch.setattr(
        home,
        "get_problem_pass_ratio",
        lambda problem_id: (0, 0),
    )
    monkeypatch.setattr(
        home,
        "get_recent_attempts",
        lambda n, problem_id: [],
    )
    monkeypatch.setattr(
        home,
        "get_best_attempts",
        lambda n, problem_id: [],
    )

    async with home_app.run_test():
        details = home_app.get_problem_details()

        assert details == (
            "# Two Sum\n\nFind two numbers.",
            Level.BREEZY,
            0,
            0,
            "...",
            "...",
        )


@pytest.mark.asyncio
async def test_get_problem_details_includes_attempt_statistics(
    home_app,
    fake_questions,
    monkeypatch,
):
    monkeypatch.setattr(
        home,
        "get_problem_pass_ratio",
        lambda problem_id: (3, 5),
    )
    monkeypatch.setattr(
        home,
        "get_recent_attempts",
        lambda n, problem_id: [
            {
                "status": RunStatus.PASSED,
                "created_at": 1000.0,
            }
        ],
    )
    monkeypatch.setattr(
        home,
        "get_best_attempts",
        lambda n, problem_id: [
            {
                "elapsed": 125.0,
            }
        ],
    )
    monkeypatch.setattr(
        home,
        "fmt_secs",
        lambda elapsed: f"{elapsed} seconds",
    )
    monkeypatch.setattr(
        home,
        "time_ago",
        lambda timestamp: f"{timestamp} ago",
    )

    async with home_app.run_test():
        details = home_app.get_problem_details()

        assert details == (
            "# Two Sum\n\nFind two numbers.",
            Level.BREEZY,
            3,
            5,
            f"{RunStatus.PASSED.icon} 1000.0 ago",
            "125.0 seconds",
        )


@pytest.mark.asyncio
async def test_get_problem_details_uses_failed_status_icon(
    home_app,
    fake_questions,
    monkeypatch,
):
    monkeypatch.setattr(
        home,
        "get_problem_pass_ratio",
        lambda problem_id: (0, 1),
    )
    monkeypatch.setattr(
        home,
        "get_recent_attempts",
        lambda n, problem_id: [
            {
                "status": RunStatus.FAILED,
                "created_at": 1000.0,
            }
        ],
    )
    monkeypatch.setattr(
        home,
        "get_best_attempts",
        lambda n, problem_id: [],
    )
    monkeypatch.setattr(
        home,
        "time_ago",
        lambda timestamp: "1 min ago",
    )

    async with home_app.run_test():
        details = home_app.get_problem_details()

        assert details[4] == f"{RunStatus.FAILED.icon} 1 min ago"


# Problem rendering
@pytest.mark.asyncio
async def test_home_updates_problem_view(home_app, monkeypatch):
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

        markdown = home_app.query_one(Markdown)
        passed = home_app.query_one("#passed", Static)
        last = home_app.query_one("#last", Static)
        best = home_app.query_one("#best", Static)
        level = home_app.query_one("#level", Static)

        assert str(markdown.source) == "# Two Sum"
        assert str(passed.content) == "2/4"
        assert str(last.content) == "✓ 1 min ago"
        assert str(best.content) == "5 mins"
        assert "Breezy" in str(level.content)


# Navigation
@pytest.mark.asyncio
async def test_action_next_moves_to_next_problem(home_app):
    async with home_app.run_test():
        home_app.action_next()

        assert home_app.index == 1
        assert home_app.problem_id == 2


@pytest.mark.asyncio
async def test_action_next_does_not_move_past_last_problem(home_app):
    async with home_app.run_test():
        home_app.index = home_app.problems_count - 1

        home_app.action_next()

        assert home_app.index == home_app.problems_count - 1
        assert home_app.problem_id == 3


@pytest.mark.asyncio
async def test_action_previous_moves_to_previous_problem(home_app):
    async with home_app.run_test():
        home_app.index = 2

        home_app.action_previous()

        assert home_app.index == 1
        assert home_app.problem_id == 2


@pytest.mark.asyncio
async def test_action_previous_does_not_move_before_first_problem(home_app):
    async with home_app.run_test():
        home_app.action_previous()

        assert home_app.index == 0
        assert home_app.problem_id == 1


@pytest.mark.asyncio
async def test_next_hides_dashboard(home_app):
    async with home_app.run_test():
        home_app.show_dashboard = True

        home_app.action_next()

        assert home_app.show_dashboard is False


@pytest.mark.asyncio
async def test_previous_hides_dashboard(home_app):
    async with home_app.run_test():
        home_app.show_dashboard = True

        home_app.action_previous()

        assert home_app.show_dashboard is False


# Dashboard
@pytest.mark.asyncio
async def test_action_dashboard_toggles_visibility(home_app):
    async with home_app.run_test():
        assert home_app.show_dashboard is False

        home_app.action_dashboard()
        assert home_app.show_dashboard is True

        home_app.action_dashboard()
        assert home_app.show_dashboard is False


@pytest.mark.asyncio
async def test_show_dashboard_updates_dashboard_class(home_app):
    async with home_app.run_test():
        dashboard = home_app.query_one(home.Dashboard)

        assert not dashboard.has_class("-visible")

        home_app.show_dashboard = True

        assert dashboard.has_class("-visible")

        home_app.show_dashboard = False

        assert not dashboard.has_class("-visible")


# Attempt action
@pytest.mark.asyncio
async def test_action_attempt_defaults_to_python_when_no_recent_attempt(
    home_app,
    monkeypatch,
):
    captured = {}

    def fake_get_recent_attempts(*, n, problem_id=None):
        return []

    def fake_get_draft(*, problem_id, lang_id):
        captured["problem_id"] = problem_id
        captured["lang_id"] = lang_id

    monkeypatch.setattr(home, "AttemptScreen", FakeAttemptScreen)
    monkeypatch.setattr(home, "get_recent_attempts", fake_get_recent_attempts)
    monkeypatch.setattr(home, "get_draft", fake_get_draft)

    async with home_app.run_test() as pilot:
        home_app.action_attempt()
        await pilot.pause()

        assert captured == {
            "problem_id": 1,
            "lang_id": Language.PYTHON,
        }

        assert isinstance(home_app.screen, FakeAttemptScreen)
        assert home_app.screen.problem_id == 1
        assert home_app.screen.language is Language.PYTHON
        assert home_app.screen.draft is None


@pytest.mark.asyncio
async def test_action_attempt_uses_language_from_recent_attempt(
    home_app,
    monkeypatch,
):
    captured = {}

    def fake_get_recent_attempts(*, n, problem_id=None):
        return [
            {
                "created_at": 1_000.0,
                "lang_id": Language.RUST,
                "status": RunStatus.PASSED,
            }
        ]

    def fake_get_draft(*, problem_id, lang_id):
        captured["problem_id"] = problem_id
        captured["lang_id"] = lang_id
        return "draft"

    monkeypatch.setattr(home, "AttemptScreen", FakeAttemptScreen)
    monkeypatch.setattr(home, "get_recent_attempts", fake_get_recent_attempts)
    monkeypatch.setattr(home, "get_draft", fake_get_draft)

    async with home_app.run_test() as pilot:
        home_app.action_attempt()
        await pilot.pause()

        assert captured == {
            "problem_id": 1,
            "lang_id": Language.RUST,
        }

        assert isinstance(home_app.screen, FakeAttemptScreen)
        assert home_app.screen.problem_id == 1
        assert home_app.screen.language is Language.RUST
        assert home_app.screen.draft == "draft"


@pytest.mark.asyncio
async def test_action_attempt_hides_dashboard(
    home_app,
    monkeypatch,
):

    def fake_get_recent_attempts(*, n, problem_id=None):
        return None

    def fake_get_draft(*, problem_id, lang_id):
        return None

    monkeypatch.setattr(home, "AttemptScreen", FakeAttemptScreen)
    monkeypatch.setattr(home, "get_recent_attempts", fake_get_recent_attempts)
    monkeypatch.setattr(home, "get_draft", fake_get_draft)

    async with home_app.run_test() as pilot:
        home_app.show_dashboard = True

        home_app.action_attempt()
        await pilot.pause()

        assert home_app.show_dashboard is False


# Search action
@pytest.mark.asyncio
async def test_action_search_hides_dashboard(
    home_app,
    monkeypatch,
):
    monkeypatch.setattr(home, "SearchScreen", FakeSearchScreen)

    async with home_app.run_test():
        home_app.show_dashboard = True

        home_app.action_search()

        assert home_app.show_dashboard is False
        assert isinstance(home_app.screen, FakeSearchScreen)


@pytest.mark.asyncio
async def test_search_callback_selects_existing_problem(
    home_app,
    monkeypatch,
):
    monkeypatch.setattr(home, "SearchScreen", FakeSearchScreen)

    callback = None

    def push_screen(screen, on_close):
        nonlocal callback
        callback = on_close

    monkeypatch.setattr(home_app, "push_screen", push_screen)

    async with home_app.run_test():
        home_app.action_search()

        assert callback is not None

        callback(3)

        assert home_app.index == 2
        assert home_app.problem_id == 3


@pytest.mark.asyncio
async def test_search_callback_ignores_unknown_problem(
    home_app,
    monkeypatch,
):
    monkeypatch.setattr(home, "SearchScreen", FakeSearchScreen)

    callback = None

    def push_screen(screen, on_close):
        nonlocal callback
        callback = on_close

    monkeypatch.setattr(home_app, "push_screen", push_screen)

    async with home_app.run_test():
        home_app.index = 1

        home_app.action_search()

        assert callback is not None

        callback(999)

        assert home_app.index == 1


@pytest.mark.asyncio
async def test_search_callback_ignores_cancel(
    home_app,
    monkeypatch,
):
    monkeypatch.setattr(home, "SearchScreen", FakeSearchScreen)

    callback = None

    def push_screen(screen, on_close):
        nonlocal callback
        callback = on_close

    monkeypatch.setattr(home_app, "push_screen", push_screen)

    async with home_app.run_test():
        home_app.index = 1

        home_app.action_search()

        assert callback is not None

        callback(None)

        assert home_app.index == 1


# Action availability
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
async def test_check_action_at_first_problem(
    home_app,
    action,
    expected,
):
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
async def test_check_action_at_last_problem(
    home_app,
    action,
    expected,
):
    async with home_app.run_test():
        home_app.index = home_app.problems_count - 1

        assert home_app.check_action(action, []) is expected


@pytest.mark.asyncio
async def test_check_action_on_intermediate_problem(home_app):
    async with home_app.run_test():
        home_app.index = 1

        assert home_app.check_action("attempt", []) is True
        assert home_app.check_action("next", []) is True
        assert home_app.check_action("previous", []) is True
        assert home_app.check_action("search", []) is True
        assert home_app.check_action("dashboard", []) is True


@pytest.mark.asyncio
async def test_check_action_hides_home_actions_on_non_default_screen(
    home_app,
):
    async with home_app.run_test():
        home_app.push_screen(FakeSearchScreen())

        assert home_app.check_action("attempt", []) is False
        assert home_app.check_action("next", []) is False
        assert home_app.check_action("previous", []) is False
        assert home_app.check_action("search", []) is False
        assert home_app.check_action("dashboard", []) is False
