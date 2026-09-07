import pytest
from textual.app import App
from textual.widgets import Footer, RichLog, Static

import algoflex.result as result_module
from algoflex.result import ResultModal
from algoflex.runner import ExecutionResult
from algoflex.types import Language, RunStatus


class FakeQuestion:
    def __init__(self, tests: str = "assert True") -> None:
        self.tests = tests

    def tests_for(self, language: Language) -> str:
        return self.tests


class FakeQuestions:
    def __init__(self) -> None:
        self._questions = {
            1: FakeQuestion("assert True"),
        }

    def get(self, problem_id: int) -> FakeQuestion:
        return self._questions[problem_id]


class HostApp(App):
    """Minimal host for testing modal-screen behavior."""


def make_modal(
    *,
    problem_id: int = 1,
    user_code: str = "print('hello')",
    elapsed: float = 12.5,
    best: float | None = None,
    language: Language = Language.PYTHON,
) -> ResultModal:
    return ResultModal(
        problem_id,
        user_code,
        elapsed,
        best,
        language,
    )


@pytest.fixture
def fake_questions(monkeypatch):
    questions = FakeQuestions()
    monkeypatch.setattr(
        result_module,
        "questions",
        questions,
    )
    return questions


@pytest.fixture
def disable_worker(monkeypatch):
    async def noop(self):
        pass

    monkeypatch.setattr(
        ResultModal,
        "run_user_code",
        noop,
    )


# Composition
@pytest.mark.asyncio
async def test_result_modal_composes_expected_widgets(disable_worker):
    app = HostApp()
    modal = make_modal()

    async with app.run_test() as pilot:
        app.push_screen(modal)
        await pilot.pause()

        assert app.screen is modal
        assert modal.query_one(RichLog)
        assert modal.query_one("#status", Static)
        assert modal.query_one(Footer)


@pytest.mark.asyncio
async def test_result_modal_starts_with_empty_status(disable_worker):
    app = HostApp()
    modal = make_modal()

    async with app.run_test() as pilot:
        app.push_screen(modal)
        await pilot.pause()

        status = modal.query_one("#status", Static)

        assert str(status.content) == ""


@pytest.mark.asyncio
async def test_result_modal_preserves_constructor_state(
    disable_worker,
):
    app = HostApp()

    modal = make_modal(
        problem_id=42,
        user_code="solution()",
        elapsed=15.75,
        best=20.0,
        language=Language.RUST,
    )

    async with app.run_test() as pilot:
        app.push_screen(modal)
        await pilot.pause()

        assert modal.problem_id == 42
        assert modal.user_code == "solution()"
        assert modal.elapsed == 15.75
        assert modal.best == 20.0
        assert modal.language is Language.RUST


# Loading spinner
@pytest.mark.asyncio
async def test_start_loading_updates_status(
    disable_worker,
):
    app = HostApp()
    modal = make_modal()

    async with app.run_test() as pilot:
        app.push_screen(modal)
        await pilot.pause()

        modal.start_loading()

        status = modal.query_one("#status", Static)

        assert str(status.content) == "⠋ Running tests..."
        assert modal._spinner_timer is not None


@pytest.mark.asyncio
async def test_start_loading_accepts_custom_message(
    disable_worker,
):
    app = HostApp()
    modal = make_modal()

    async with app.run_test() as pilot:
        app.push_screen(modal)
        await pilot.pause()

        modal.start_loading("Compiling...")

        status = modal.query_one("#status", Static)

        assert str(status.content) == "⠋ Compiling..."


@pytest.mark.asyncio
async def test_spinner_updates(
    disable_worker,
):
    app = HostApp()
    modal = make_modal()

    async with app.run_test() as pilot:
        app.push_screen(modal)
        await pilot.pause()

        modal.start_loading()

        assert modal._spinner_index == 0

        modal._update_spinner("Running tests...")

        status = modal.query_one("#status", Static)

        assert modal._spinner_index == 1
        assert str(status.content) == "⠙ Running tests..."


@pytest.mark.asyncio
async def test_stop_loading_stops_spinner_and_clears_status(
    disable_worker,
):
    app = HostApp()
    modal = make_modal()

    async with app.run_test() as pilot:
        app.push_screen(modal)
        await pilot.pause()

        modal.start_loading()
        modal.stop_loading()

        status = modal.query_one("#status", Static)

        assert modal._spinner_timer is None
        assert str(status.content) == ""


@pytest.mark.asyncio
async def test_stop_loading_is_safe_without_active_spinner(
    disable_worker,
):
    app = HostApp()
    modal = make_modal()

    async with app.run_test() as pilot:
        app.push_screen(modal)
        await pilot.pause()

        modal.stop_loading()

        status = modal.query_one("#status", Static)

        assert modal._spinner_timer is None
        assert str(status.content) == ""


# New best time taken
@pytest.mark.asyncio
async def test_show_new_best_mounts_new_best_message(
    disable_worker,
    monkeypatch,
):
    app = HostApp()
    modal = make_modal(elapsed=12.5)

    monkeypatch.setattr(
        result_module,
        "fmt_secs",
        lambda value: "12 secs",
    )

    async with app.run_test() as pilot:
        app.push_screen(modal)
        await pilot.pause()

        modal._show_new_best()

        messages = [
            widget
            for widget in modal.query(Static)
            if "New best time!!" in str(widget.render())
        ]

        assert len(messages) == 1
        assert "New best time!!" in str(messages[0].render())
        assert "12 secs" in str(messages[0].render())


@pytest.mark.asyncio
async def test_show_success_does_nothing_when_not_a_new_best(
    disable_worker,
):
    app = HostApp()
    modal = make_modal(elapsed=20.0, best=10.0)

    async with app.run_test() as pilot:
        app.push_screen(modal)
        await pilot.pause()

        modal._show_success()

        assert not any(
            "New best time!!" in str(widget.render())
            for widget in modal.query(Static)
            if widget.id != "status"
        )


@pytest.mark.asyncio
async def test_show_success_creates_new_best_when_no_previous_best(
    disable_worker,
    monkeypatch,
):
    app = HostApp()
    modal = make_modal(elapsed=20.0, best=None)

    monkeypatch.setattr(
        result_module,
        "fmt_secs",
        lambda value: "20 secs",
    )

    async with app.run_test() as pilot:
        app.push_screen(modal)
        await pilot.pause()

        modal._show_success()

        assert any(
            "New best time!!" in str(widget.render())
            for widget in modal.query(Static)
            if widget.id != "status"
        )


@pytest.mark.asyncio
async def test_show_success_creates_new_best_when_faster(
    disable_worker,
    monkeypatch,
):
    app = HostApp()
    modal = make_modal(elapsed=10.0, best=20.0)

    monkeypatch.setattr(
        result_module,
        "fmt_secs",
        lambda value: "10 secs",
    )

    async with app.run_test() as pilot:
        app.push_screen(modal)
        await pilot.pause()

        modal._show_success()

        assert any(
            "New best time!!" in str(widget.render())
            for widget in modal.query(Static)
            if widget.id != "status"
        )


@pytest.mark.asyncio
async def test_show_success_does_not_create_new_best_when_equal(
    disable_worker,
):
    app = HostApp()
    modal = make_modal(elapsed=10.0, best=10.0)

    async with app.run_test() as pilot:
        app.push_screen(modal)
        await pilot.pause()

        modal._show_success()

        assert not any(
            "New best time!!" in str(widget.render())
            for widget in modal.query(Static)
            if widget.id != "status"
        )


# Saving results
def test_save_passed_result_adds_attempt_and_deletes_draft(
    monkeypatch,
):
    captured = {}

    def fake_add_attempt(attempt):
        captured["attempt"] = attempt

    def fake_delete_draft(problem_id, language):
        captured["deleted"] = (problem_id, language)

    monkeypatch.setattr(
        result_module,
        "add_attempt",
        fake_add_attempt,
    )
    monkeypatch.setattr(
        result_module,
        "delete_draft",
        fake_delete_draft,
    )

    modal = make_modal(
        problem_id=7,
        user_code="  print('hello')  ",
        elapsed=15.0,
        language=Language.PYTHON,
    )

    modal._save_result(
        status=RunStatus.PASSED,
        created_at=1234.5,
    )

    assert captured["attempt"] == {
        "problem_id": 7,
        "status": RunStatus.PASSED,
        "elapsed": 15.0,
        "created_at": 1234.5,
        "code": "print('hello')",
        "lang_id": Language.PYTHON,
    }

    assert captured["deleted"] == (
        7,
        Language.PYTHON,
    )


def test_save_failed_result_adds_attempt_and_saves_draft(
    monkeypatch,
):
    captured = {}

    def fake_add_attempt(attempt):
        captured["attempt"] = attempt

    def fake_add_draft(draft):
        captured["draft"] = draft

    monkeypatch.setattr(
        result_module,
        "add_attempt",
        fake_add_attempt,
    )
    monkeypatch.setattr(
        result_module,
        "add_draft",
        fake_add_draft,
    )

    modal = make_modal(
        problem_id=7,
        user_code="  broken()  ",
        elapsed=25.5,
        language=Language.RUST,
    )

    modal._save_result(
        status=RunStatus.FAILED,
        created_at=1234.5,
    )

    assert captured["attempt"] == {
        "problem_id": 7,
        "status": RunStatus.FAILED,
        "elapsed": 25.5,
        "created_at": 1234.5,
        "code": "broken()",
        "lang_id": Language.RUST,
    }

    assert captured["draft"] == {
        "problem_id": 7,
        "lang_id": Language.RUST,
        "code": "broken()",
        "elapsed": 25.5,
        "updated_at": 1234.5,
    }


@pytest.mark.parametrize(
    "status",
    [
        RunStatus.FAILED,
        RunStatus.COMPILE_ERROR,
        RunStatus.TIMEOUT,
        RunStatus.ERROR,
    ],
)
def test_unsuccessful_result_saves_draft(
    monkeypatch,
    status,
):
    attempts = []
    drafts = []
    deleted = []

    monkeypatch.setattr(
        result_module,
        "add_attempt",
        attempts.append,
    )
    monkeypatch.setattr(
        result_module,
        "add_draft",
        drafts.append,
    )
    monkeypatch.setattr(
        result_module,
        "delete_draft",
        lambda *args: deleted.append(args),
    )

    modal = make_modal(
        user_code="solution()",
        elapsed=8.0,
        language=Language.PYTHON,
    )

    modal._save_result(
        status=status,
        created_at=100.0,
    )

    assert len(attempts) == 1
    assert len(drafts) == 1
    assert deleted == []


def test_save_result_strips_user_code(
    monkeypatch,
):
    captured = {}

    monkeypatch.setattr(
        result_module,
        "add_attempt",
        lambda value: captured.setdefault("attempt", value),
    )
    monkeypatch.setattr(
        result_module,
        "add_draft",
        lambda value: captured.setdefault("draft", value),
    )

    modal = make_modal(
        user_code="\n\n  print('hello')  \n\n",
    )

    modal._save_result(
        status=RunStatus.FAILED,
        created_at=100.0,
    )

    assert captured["attempt"]["code"] == "print('hello')"
    assert captured["draft"]["code"] == "print('hello')"


# Running user code
@pytest.mark.asyncio
async def test_run_user_code_uses_problem_tests_and_saves_passed_result(
    fake_questions,
    monkeypatch,
):
    captured = {}

    async def fake_run_solution(
        user_code,
        test_code,
        language,
        *,
        on_line,
    ):
        captured["user_code"] = user_code
        captured["test_code"] = test_code
        captured["language"] = language
        captured["on_line"] = on_line

        return ExecutionResult(
            status=RunStatus.PASSED,
        )

    saved = {}

    def fake_save_result(self, *, status, created_at):
        saved["status"] = status
        saved["created_at"] = created_at

    monkeypatch.setattr(
        result_module,
        "run_solution",
        fake_run_solution,
    )
    monkeypatch.setattr(
        result_module.time,
        "time",
        lambda: 1234.5,
    )
    monkeypatch.setattr(
        ResultModal,
        "_save_result",
        fake_save_result,
    )
    monkeypatch.setattr(
        ResultModal,
        "_show_success",
        lambda self: None,
    )
    monkeypatch.setattr(
        ResultModal,
        "start_loading",
        lambda self: None,
    )
    monkeypatch.setattr(
        ResultModal,
        "stop_loading",
        lambda self: None,
    )

    modal = make_modal(
        problem_id=1,
        user_code="solution()",
        language=Language.PYTHON,
    )

    await modal.run_user_code()

    assert captured["user_code"] == "solution()"
    assert captured["test_code"] == "assert True"
    assert captured["language"] is Language.PYTHON
    assert callable(captured["on_line"])

    assert saved == {
        "status": RunStatus.PASSED,
        "created_at": 1234.5,
    }


@pytest.mark.asyncio
async def test_run_user_code_shows_compile_error(
    fake_questions,
    monkeypatch,
):
    messages = []
    saved = {}

    async def fake_run_solution(*args, **kwargs):
        return ExecutionResult(
            status=RunStatus.COMPILE_ERROR,
            stderr="expected `;`",
        )

    monkeypatch.setattr(
        result_module,
        "run_solution",
        fake_run_solution,
    )
    monkeypatch.setattr(
        result_module.time,
        "time",
        lambda: 100.0,
    )
    monkeypatch.setattr(
        ResultModal,
        "start_loading",
        lambda self: None,
    )
    monkeypatch.setattr(
        ResultModal,
        "stop_loading",
        lambda self: None,
    )
    monkeypatch.setattr(
        ResultModal,
        "_show_error",
        lambda self, title, message: messages.append((title, message)),
    )
    monkeypatch.setattr(
        ResultModal,
        "_save_result",
        lambda self, **kwargs: saved.update(kwargs),
    )

    modal = make_modal()

    await modal.run_user_code()

    assert messages == [
        ("compilation failed", "expected `;`"),
    ]
    assert saved["status"] is RunStatus.COMPILE_ERROR
    assert saved["created_at"] == 100.0


@pytest.mark.asyncio
async def test_run_user_code_shows_timeout(
    fake_questions,
    monkeypatch,
):
    messages = []

    async def fake_run_solution(*args, **kwargs):
        return ExecutionResult(
            status=RunStatus.TIMEOUT,
        )

    monkeypatch.setattr(
        result_module,
        "run_solution",
        fake_run_solution,
    )
    monkeypatch.setattr(
        result_module.time,
        "time",
        lambda: 100.0,
    )
    monkeypatch.setattr(
        ResultModal,
        "start_loading",
        lambda self: None,
    )
    monkeypatch.setattr(
        ResultModal,
        "stop_loading",
        lambda self: None,
    )
    monkeypatch.setattr(
        ResultModal,
        "_show_error",
        lambda self, title, message: messages.append((title, message)),
    )
    monkeypatch.setattr(
        ResultModal,
        "_save_result",
        lambda self, **kwargs: None,
    )

    modal = make_modal()

    await modal.run_user_code()

    assert messages == [
        (
            "timed out",
            "your solution must run within 9 seconds.",
        ),
    ]


@pytest.mark.asyncio
async def test_run_user_code_shows_runtime_error(
    fake_questions,
    monkeypatch,
):
    messages = []

    async def fake_run_solution(*args, **kwargs):
        return ExecutionResult(
            status=RunStatus.ERROR,
            stderr="segmentation fault",
        )

    monkeypatch.setattr(
        result_module,
        "run_solution",
        fake_run_solution,
    )
    monkeypatch.setattr(
        result_module.time,
        "time",
        lambda: 100.0,
    )
    monkeypatch.setattr(
        ResultModal,
        "start_loading",
        lambda self: None,
    )
    monkeypatch.setattr(
        ResultModal,
        "stop_loading",
        lambda self: None,
    )
    monkeypatch.setattr(
        ResultModal,
        "_show_error",
        lambda self, title, message: messages.append((title, message)),
    )
    monkeypatch.setattr(
        ResultModal,
        "_save_result",
        lambda self, **kwargs: None,
    )

    modal = make_modal()

    await modal.run_user_code()

    assert messages == [
        ("error running code", "segmentation fault"),
    ]


@pytest.mark.asyncio
async def test_run_user_code_shows_success(
    fake_questions,
    monkeypatch,
):
    called = False

    async def fake_run_solution(*args, **kwargs):
        return ExecutionResult(
            status=RunStatus.PASSED,
        )

    def fake_show_success(self):
        nonlocal called
        called = True

    monkeypatch.setattr(
        result_module,
        "run_solution",
        fake_run_solution,
    )
    monkeypatch.setattr(
        result_module.time,
        "time",
        lambda: 100.0,
    )
    monkeypatch.setattr(
        ResultModal,
        "start_loading",
        lambda self: None,
    )
    monkeypatch.setattr(
        ResultModal,
        "stop_loading",
        lambda self: None,
    )
    monkeypatch.setattr(
        ResultModal,
        "_show_success",
        fake_show_success,
    )
    monkeypatch.setattr(
        ResultModal,
        "_save_result",
        lambda self, **kwargs: None,
    )

    modal = make_modal()

    await modal.run_user_code()

    assert called is True


# Dismissal
@pytest.mark.asyncio
async def test_escape_dismisses_result_modal(disable_worker):
    app = HostApp()

    async with app.run_test() as pilot:
        modal = make_modal()

        app.push_screen(modal)
        await pilot.pause()

        assert app.screen is modal

        await pilot.press("escape")
        await pilot.pause()

        assert app.screen is not modal


# Best-time behavior
@pytest.mark.parametrize(
    ("elapsed", "best", "is_new_best"),
    [
        (10.0, None, True),
        (10.0, 20.0, True),
        (20.0, 10.0, False),
        (10.0, 10.0, False),
    ],
)
def test_new_best_condition(elapsed, best, is_new_best):
    modal = make_modal(
        elapsed=elapsed,
        best=best,
    )

    assert (modal.best is None or modal.elapsed < modal.best) is is_new_best
