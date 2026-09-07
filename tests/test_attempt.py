import pytest
from textual.app import App
from textual.screen import Screen
from textual.widgets import Markdown, Static, TabbedContent, TextArea

from algoflex import attempt
from algoflex.attempt import AttemptScreen
from algoflex.custom_widgets import Title
from algoflex.types import Language, Level, RunStatus


class FakeQuestion:
    def __init__(
        self,
        markdown: str = "# Problem",
        level: Level = Level.BREEZY,
        starters: dict[Language, str] | None = None,
    ) -> None:
        self.markdown = markdown
        self.level = level
        self._starters = starters or {
            Language.PYTHON: "def solution():\n    pass",
            Language.RUST: "fn main() {\n}",
        }

    def starter_for(self, language: Language) -> str:
        return self._starters[language]


class FakeQuestions:
    def __init__(self) -> None:
        self._questions = {
            1: FakeQuestion(
                markdown="# Two Sum\n\nFind two numbers.",
            ),
            2: FakeQuestion(
                markdown="# Binary Search\n\nSearch a sorted array.",
                level=Level.STEADY,
            ),
        }

    def get(self, problem_id: int) -> FakeQuestion:
        return self._questions[problem_id]


class FakeResultModal(Screen):
    def __init__(
        self,
        problem_id: int,
        code: str,
        elapsed: float,
        best: float | None,
        language: Language,
    ) -> None:
        super().__init__()
        self.problem_id = problem_id
        self.code = code
        self.elapsed = elapsed
        self.best = best
        self.language = language


class AttemptApp(App):
    """Minimal host app for testing AttemptScreen."""


def push_attempt(
    app: AttemptApp,
    *,
    problem_id: int = 1,
    language: Language = Language.PYTHON,
    draft=None,
) -> AttemptScreen:
    screen = AttemptScreen(
        problem_id,
        language,
        draft,
    )
    app.push_screen(screen)
    return screen


@pytest.fixture
def fake_questions(monkeypatch):
    questions = FakeQuestions()
    monkeypatch.setattr(attempt, "questions", questions)
    return questions


@pytest.fixture
def no_attempts(monkeypatch):
    monkeypatch.setattr(
        attempt,
        "get_recent_attempts",
        lambda *, n, problem_id: [],
    )
    monkeypatch.setattr(
        attempt,
        "get_best_attempts",
        lambda *, n, problem_id: [],
    )


@pytest.fixture
def attempt_app(fake_questions, no_attempts):
    return AttemptApp()


# Composition
@pytest.mark.asyncio
async def test_attempt_composes_expected_widgets(attempt_app):
    async with attempt_app.run_test() as pilot:
        push_attempt(attempt_app)
        await pilot.pause()

        assert attempt_app.screen.query_one("#code", TextArea)
        assert attempt_app.screen.query_one("#timeline", Static)
        assert attempt_app.screen.query_one("#solutions", Markdown)
        assert attempt_app.screen.query_one("#editor", TabbedContent)


@pytest.mark.asyncio
async def test_attempt_uses_language_starter_code(attempt_app):
    async with attempt_app.run_test() as pilot:
        push_attempt(attempt_app)
        await pilot.pause()

        editor = attempt_app.screen.query_one("#code", TextArea)

        assert editor.text == "def solution():\n    pass"
        assert editor.language == Language.PYTHON.slug


@pytest.mark.asyncio
async def test_attempt_uses_requested_rust_starter_code(
    attempt_app,
):
    async with attempt_app.run_test() as pilot:
        push_attempt(
            attempt_app,
            language=Language.RUST,
        )
        await pilot.pause()

        editor = attempt_app.screen.query_one("#code", TextArea)

        assert editor.text == "fn main() {\n}"
        assert editor.language == Language.RUST.slug


@pytest.mark.asyncio
async def test_attempt_uses_draft_instead_of_starter_code(
    attempt_app,
):
    draft = {
        "code": "print('saved draft')",
        "elapsed": 12.5,
    }

    async with attempt_app.run_test() as pilot:
        push_attempt(
            attempt_app,
            draft=draft,
        )
        await pilot.pause()

        editor = attempt_app.screen.query_one("#code", TextArea)

        assert editor.text == "print('saved draft')"


# Timeline
def test_get_timeline_empty_attempts(
    fake_questions,
    monkeypatch,
):
    monkeypatch.setattr(
        attempt,
        "get_best_attempts",
        lambda *, n, problem_id: [],
    )

    screen = AttemptScreen(
        1,
        Language.PYTHON,
        None,
    )

    assert screen.get_timeline([]) == ""


def test_get_timeline_formats_attempts(
    fake_questions,
    monkeypatch,
):
    attempts = [
        {
            "attempt_id": 1,
            "status": RunStatus.PASSED,
            "created_at": 100.0,
            "elapsed": 65.0,
            "lang_id": Language.PYTHON,
        },
        {
            "attempt_id": 2,
            "status": RunStatus.FAILED,
            "created_at": 200.0,
            "elapsed": 120.0,
            "lang_id": Language.RUST,
        },
    ]

    monkeypatch.setattr(
        attempt,
        "get_best_attempts",
        lambda *, n, problem_id: [],
    )
    monkeypatch.setattr(
        attempt,
        "time_ago",
        lambda value: f"{value} ago",
    )
    monkeypatch.setattr(
        attempt,
        "fmt_secs",
        lambda value: f"{value}s",
    )

    screen = AttemptScreen(
        1,
        Language.PYTHON,
        None,
    )

    result = screen.get_timeline(attempts)

    assert "100.0 ago" in result
    assert "200.0 ago" in result
    assert "65.0s" in result
    assert "120.0s" in result
    assert Language.PYTHON.icon in result
    assert Language.RUST.icon in result
    assert RunStatus.PASSED.icon in result
    assert RunStatus.FAILED.icon in result


def test_get_timeline_marks_best_attempt(
    fake_questions,
    monkeypatch,
):
    attempts = [
        {
            "attempt_id": 1,
            "status": RunStatus.PASSED,
            "created_at": 100.0,
            "elapsed": 65.0,
            "lang_id": Language.PYTHON,
        },
        {
            "attempt_id": 2,
            "status": RunStatus.PASSED,
            "created_at": 200.0,
            "elapsed": 120.0,
            "lang_id": Language.RUST,
        },
    ]

    monkeypatch.setattr(
        attempt,
        "get_best_attempts",
        lambda *, n, problem_id: [attempts[0]],
    )
    monkeypatch.setattr(
        attempt,
        "time_ago",
        lambda _: "1 min ago",
    )
    monkeypatch.setattr(
        attempt,
        "fmt_secs",
        lambda _: "1 min",
    )

    screen = AttemptScreen(
        1,
        Language.PYTHON,
        None,
    )

    result = screen.get_timeline(attempts)

    assert "<--- best" in result
    assert screen.best == 65.0


def test_get_timeline_stores_best_elapsed(
    fake_questions,
    monkeypatch,
):
    best = {
        "attempt_id": 10,
        "elapsed": 42.5,
    }

    monkeypatch.setattr(
        attempt,
        "get_best_attempts",
        lambda *, n, problem_id: [best],
    )

    screen = AttemptScreen(
        1,
        Language.PYTHON,
        None,
    )

    screen.get_timeline([])

    assert screen.best == 42.5


# Solutions
def test_get_solutions_only_includes_passed_attempts(
    fake_questions,
    monkeypatch,
):
    attempts = [
        {
            "status": RunStatus.PASSED,
            "created_at": 100.0,
            "lang_id": Language.PYTHON,
            "code": "print('hello')",
        },
        {
            "status": RunStatus.FAILED,
            "created_at": 200.0,
            "lang_id": Language.RUST,
            "code": "broken code",
        },
    ]

    monkeypatch.setattr(
        attempt,
        "time_ago",
        lambda value: f"{value} ago",
    )

    screen = AttemptScreen(
        1,
        Language.PYTHON,
        None,
    )

    result = screen.get_solutions(attempts)

    assert "print('hello')" in result
    assert "broken code" not in result
    assert Language.PYTHON.icon in result
    assert "100.0 ago" in result


def test_get_solutions_supports_multiple_languages(
    fake_questions,
    monkeypatch,
):
    attempts = [
        {
            "status": RunStatus.PASSED,
            "created_at": 100.0,
            "lang_id": Language.PYTHON,
            "code": "print('python')",
        },
        {
            "status": RunStatus.PASSED,
            "created_at": 200.0,
            "lang_id": Language.RUST,
            "code": 'println!("rust");',
        },
    ]

    monkeypatch.setattr(
        attempt,
        "time_ago",
        lambda _: "1 min ago",
    )

    screen = AttemptScreen(
        1,
        Language.PYTHON,
        None,
    )

    result = screen.get_solutions(attempts)

    assert "print('python')" in result
    assert 'println!("rust");' in result
    assert f"```{Language.PYTHON.slug}" in result
    assert f"```{Language.RUST.slug}" in result


def test_get_solutions_returns_empty_string_for_no_attempts(
    fake_questions,
):
    screen = AttemptScreen(
        1,
        Language.PYTHON,
        None,
    )

    assert screen.get_solutions([]) == ""


# Attempt view
@pytest.mark.asyncio
async def test_update_attempt_view_loads_recent_attempts(
    attempt_app,
    monkeypatch,
):
    recent = [
        {
            "attempt_id": 1,
            "status": RunStatus.PASSED,
            "created_at": 100.0,
            "elapsed": 60.0,
            "lang_id": Language.PYTHON,
            "code": "print('hello')",
        }
    ]

    monkeypatch.setattr(
        attempt,
        "get_recent_attempts",
        lambda *, n, problem_id: recent,
    )
    monkeypatch.setattr(
        attempt,
        "get_best_attempts",
        lambda *, n, problem_id: [],
    )
    monkeypatch.setattr(
        attempt,
        "time_ago",
        lambda _: "1 min ago",
    )
    monkeypatch.setattr(
        attempt,
        "fmt_secs",
        lambda _: "1 min",
    )

    async with attempt_app.run_test() as pilot:
        screen = push_attempt(attempt_app)
        await pilot.pause()

        screen.update_attempt_view()

        assert "1 min ago" in str(screen.timeline.content)
        assert "print('hello')" in screen.solutions.source


# Submit
@pytest.mark.asyncio
async def test_submit_pushes_result_modal(
    attempt_app,
    monkeypatch,
):
    monkeypatch.setattr(
        attempt,
        "ResultModal",
        FakeResultModal,
    )
    monkeypatch.setattr(
        attempt,
        "monotonic",
        lambda: 110.0,
    )

    async with attempt_app.run_test() as pilot:
        screen = push_attempt(attempt_app)
        await pilot.pause()

        captured = {}

        def fake_push_screen(screen, callback=None):
            captured["screen"] = screen
            captured["callback"] = callback

        monkeypatch.setattr(
            attempt_app,
            "push_screen",
            fake_push_screen,
        )

        screen.test_time = 100.0

        editor = screen.query_one("#code", TextArea)
        editor.text = "print('solution')"

        screen.submit()

        result = captured["screen"]

        assert isinstance(result, FakeResultModal)
        assert result.problem_id == 1
        assert result.code == "print('solution')"
        assert result.language is Language.PYTHON
        assert result.elapsed == 10.0
        assert result.best is None
        assert callable(captured["callback"])


@pytest.mark.asyncio
async def test_submit_includes_draft_elapsed_time(
    attempt_app,
    monkeypatch,
):
    draft = {
        "code": "saved",
        "elapsed": 25.0,
    }

    monkeypatch.setattr(
        attempt,
        "ResultModal",
        FakeResultModal,
    )
    monkeypatch.setattr(
        attempt,
        "monotonic",
        lambda: 110.0,
    )

    async with attempt_app.run_test() as pilot:
        screen = push_attempt(
            attempt_app,
            draft=draft,
        )
        await pilot.pause()

        captured = {}

        def fake_push_screen(screen, callback=None):
            captured["screen"] = screen
            captured["callback"] = callback

        monkeypatch.setattr(
            attempt_app,
            "push_screen",
            fake_push_screen,
        )

        screen.test_time = 100.0

        screen.submit()

        assert captured["screen"].elapsed == 35.0


# Draft
def test_load_draft_uses_current_problem_and_language(
    fake_questions,
    monkeypatch,
):
    captured = {}

    def fake_get_draft(*, problem_id, lang_id):
        captured["problem_id"] = problem_id
        captured["lang_id"] = lang_id
        return "draft"

    monkeypatch.setattr(
        attempt,
        "get_draft",
        fake_get_draft,
    )

    screen = AttemptScreen(
        2,
        Language.RUST,
        None,
    )

    assert screen.load_draft() == "draft"
    assert captured == {
        "problem_id": 2,
        "lang_id": Language.RUST,
    }


# Actions
@pytest.mark.asyncio
async def test_action_submit_calls_submit(
    attempt_app,
    monkeypatch,
):
    called = False

    def fake_submit():
        nonlocal called
        called = True

    async with attempt_app.run_test() as pilot:
        screen = push_attempt(attempt_app)
        await pilot.pause()

        monkeypatch.setattr(screen, "submit", fake_submit)

        screen.action_submit()

        assert called is True


@pytest.mark.asyncio
async def test_action_back_dismisses_screen(
    attempt_app,
):
    async with attempt_app.run_test() as pilot:
        push_attempt(attempt_app)
        await pilot.pause()

        assert isinstance(attempt_app.screen, AttemptScreen)

        attempt_app.screen.action_back()
        await pilot.pause()

        assert not isinstance(attempt_app.screen, AttemptScreen)


# Language changes
@pytest.mark.asyncio
async def test_update_language_changes_editor_language(
    attempt_app,
    monkeypatch,
):
    async with attempt_app.run_test() as pilot:
        screen = push_attempt(attempt_app)
        await pilot.pause()

        monkeypatch.setattr(
            screen,
            "load_draft",
            lambda: None,
        )

        screen.update_language(Language.RUST)

        editor = screen.query_one("#code", TextArea)

        assert screen.language is Language.RUST
        assert editor.language == Language.RUST.slug
        assert editor.text == "fn main() {\n}"


@pytest.mark.asyncio
async def test_update_language_uses_language_specific_draft(
    attempt_app,
    monkeypatch,
):
    draft = {
        "code": 'fn main() {\n    println!("saved");\n}',
    }

    async with attempt_app.run_test() as pilot:
        screen = push_attempt(attempt_app)
        await pilot.pause()

        monkeypatch.setattr(
            screen,
            "load_draft",
            lambda: draft,
        )

        screen.update_language(Language.RUST)

        editor = screen.query_one("#code", TextArea)

        assert screen.language is Language.RUST
        assert editor.language == Language.RUST.slug
        assert editor.text == draft["code"]


@pytest.mark.asyncio
async def test_update_language_uses_starter_when_no_draft(
    attempt_app,
    monkeypatch,
):
    async with attempt_app.run_test() as pilot:
        screen = push_attempt(attempt_app)
        await pilot.pause()

        monkeypatch.setattr(
            screen,
            "load_draft",
            lambda: None,
        )

        screen.update_language(Language.RUST)

        editor = screen.query_one("#code", TextArea)

        assert screen.language is Language.RUST
        assert editor.language == Language.RUST.slug
        assert editor.text == "fn main() {\n}"


@pytest.mark.asyncio
async def test_same_language_change_does_not_reload(
    attempt_app,
    monkeypatch,
):
    called = False

    def fake_update_language(language):
        nonlocal called
        called = True

    async with attempt_app.run_test() as pilot:
        screen = push_attempt(attempt_app)
        await pilot.pause()

        monkeypatch.setattr(
            screen,
            "update_language",
            fake_update_language,
        )

        title = screen.query_one(Title)

        screen.on_title_language_changed(title.LanguageChanged(Language.PYTHON))

        assert called is False


@pytest.mark.asyncio
async def test_different_language_change_updates_language(
    attempt_app,
    monkeypatch,
):
    captured = {}

    def fake_update_language(language):
        captured["language"] = language

    async with attempt_app.run_test() as pilot:
        screen = push_attempt(attempt_app)
        await pilot.pause()

        monkeypatch.setattr(
            screen,
            "update_language",
            fake_update_language,
        )

        title = screen.query_one(Title)

        screen.on_title_language_changed(title.LanguageChanged(Language.RUST))

        assert captured == {
            "language": Language.RUST,
        }
