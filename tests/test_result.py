from types import SimpleNamespace

import pytest
from textual.app import App
from textual.widgets import Footer, RichLog, Static

import algoflex.result as result_module
from algoflex.result import ResultModal
from algoflex.runner import ExecutionResult
from algoflex.types import Language, RunStatus


# Test doubles and helpers
class FakeQuestion:
    def __init__(
        self,
        question_id: int = 1,
        tests: str = "assert True",
    ) -> None:
        self.id = question_id
        self.tests = tests

    def tests_for(self, language: Language) -> str:
        return self.tests


class HostApp(App):
    """Minimal host for testing modal-screen behavior."""


def make_modal(
    *,
    question: FakeQuestion | None = None,
    user_code: str = "print('hello')",
    elapsed: float = 12.5,
    best: float | None = None,
    language: Language = Language.PYTHON,
) -> ResultModal:
    return ResultModal(
        question or FakeQuestion(),
        user_code,
        elapsed,
        best,
        language,
    )


def find_new_best_indicator(modal: ResultModal) -> str | None:
    """Return the rendered text of the new-best Static, or None if absent."""
    for widget in modal.query(Static):
        if widget.id == "status":
            continue
        text = str(widget.render())
        if "New best time!!" in text:
            return text
    return None


def stub_attempt_persistence(monkeypatch) -> SimpleNamespace:
    """Patch attempt/draft persistence and capture what was written.

    The returned namespace has .attempts, .drafts, and .deleted lists.
    """
    cap = SimpleNamespace(attempts=[], drafts=[], deleted=[])

    monkeypatch.setattr(result_module, "add_attempt", cap.attempts.append)
    monkeypatch.setattr(result_module, "add_draft", cap.drafts.append)
    monkeypatch.setattr(
        result_module,
        "delete_draft",
        lambda problem_id, language: cap.deleted.append((problem_id, language)),
    )

    return cap


def stub_run_user_code(monkeypatch, *, result, created_at=100.0) -> SimpleNamespace:
    """Patch run_user_code's collaborators and return a capture namespace.

    The namespace has:
      captured         dict of args passed to run_solution
      errors           list of (title, message) tuples from _show_error
      saved            dict of kwargs passed to _save_result
      success_called   True if _show_success was invoked
    """
    cap = SimpleNamespace(captured={}, errors=[], saved={}, success_called=False)

    async def fake_run_solution(user_code, test_code, language, *, on_line):
        cap.captured.update(
            user_code=user_code,
            test_code=test_code,
            language=language,
            on_line=on_line,
        )
        return result

    monkeypatch.setattr(result_module, "run_solution", fake_run_solution)
    monkeypatch.setattr(result_module.time, "time", lambda: created_at)
    monkeypatch.setattr(ResultModal, "start_loading", lambda self: None)
    monkeypatch.setattr(ResultModal, "stop_loading", lambda self: None)
    monkeypatch.setattr(
        ResultModal,
        "_show_error",
        lambda self, title, message: cap.errors.append((title, message)),
    )
    monkeypatch.setattr(
        ResultModal,
        "_save_result",
        lambda self, **kwargs: cap.saved.update(kwargs),
    )

    def _mark_success(self):
        cap.success_called = True

    monkeypatch.setattr(ResultModal, "_show_success", _mark_success)

    return cap


@pytest.fixture
def disable_worker(monkeypatch):
    async def noop(self):
        pass

    monkeypatch.setattr(ResultModal, "run_user_code", noop)


# Composition
class TestComposition:
    @pytest.mark.asyncio
    async def test_composes_expected_widgets(self, disable_worker):
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
    async def test_starts_with_empty_status(self, disable_worker):
        app = HostApp()
        modal = make_modal()

        async with app.run_test() as pilot:
            app.push_screen(modal)
            await pilot.pause()

            status = modal.query_one("#status", Static)

            assert str(status.content) == ""

    @pytest.mark.asyncio
    async def test_preserves_constructor_state(self, disable_worker):
        app = HostApp()
        question = FakeQuestion(question_id=42)

        modal = make_modal(
            question=question,
            user_code="solution()",
            elapsed=15.75,
            best=20.0,
            language=Language.RUST,
        )

        async with app.run_test() as pilot:
            app.push_screen(modal)
            await pilot.pause()

            assert modal.question is question
            assert modal.question.id == 42
            assert modal.user_code == "solution()"
            assert modal.elapsed == 15.75
            assert modal.best == 20.0
            assert modal.language is Language.RUST


# Loading spinner
class TestLoadingSpinner:
    @pytest.mark.asyncio
    async def test_start_loading_updates_status(self, disable_worker):
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
    async def test_start_loading_accepts_custom_message(self, disable_worker):
        app = HostApp()
        modal = make_modal()

        async with app.run_test() as pilot:
            app.push_screen(modal)
            await pilot.pause()

            modal.start_loading("Compiling...")

            status = modal.query_one("#status", Static)

            assert str(status.content) == "⠋ Compiling..."

    @pytest.mark.asyncio
    async def test_spinner_advances_frame(self, disable_worker):
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
    async def test_stop_loading_stops_spinner_and_clears_status(self, disable_worker):
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
    async def test_stop_loading_is_safe_without_active_spinner(self, disable_worker):
        app = HostApp()
        modal = make_modal()

        async with app.run_test() as pilot:
            app.push_screen(modal)
            await pilot.pause()

            modal.stop_loading()

            status = modal.query_one("#status", Static)

            assert modal._spinner_timer is None
            assert str(status.content) == ""


# New-best indicator
class TestNewBestIndicator:
    @pytest.mark.parametrize(
        ("elapsed", "best", "expected"),
        [
            (10.0, None, True),
            (10.0, 20.0, True),
            (20.0, 10.0, False),
            (10.0, 10.0, False),
        ],
    )
    @pytest.mark.asyncio
    async def test_shown_only_for_new_best(
        self, disable_worker, monkeypatch, elapsed, best, expected
    ):
        monkeypatch.setattr(result_module, "fmt_secs", lambda value: "12 secs")

        app = HostApp()
        modal = make_modal(elapsed=elapsed, best=best)

        async with app.run_test() as pilot:
            app.push_screen(modal)
            await pilot.pause()

            modal._show_success()

            assert (find_new_best_indicator(modal) is not None) is expected

    @pytest.mark.asyncio
    async def test_shows_elapsed(self, disable_worker, monkeypatch):
        monkeypatch.setattr(result_module, "fmt_secs", lambda value: "12 secs")

        app = HostApp()
        modal = make_modal(elapsed=12.5)

        async with app.run_test() as pilot:
            app.push_screen(modal)
            await pilot.pause()

            modal._show_new_best()

            text = find_new_best_indicator(modal)

            assert text is not None
            assert "12 secs" in text


# Saving results
class TestSaveResult:
    def test_passed_result_adds_attempt_and_deletes_draft(self, monkeypatch):
        cap = stub_attempt_persistence(monkeypatch)

        modal = make_modal(
            question=FakeQuestion(question_id=7),
            user_code="  print('hello')  ",
            elapsed=15.0,
            language=Language.PYTHON,
        )

        modal._save_result(status=RunStatus.PASSED, created_at=1234.5)

        assert cap.attempts == [
            {
                "problem_id": 7,
                "status": RunStatus.PASSED,
                "elapsed": 15.0,
                "created_at": 1234.5,
                "code": "print('hello')",
                "lang_id": Language.PYTHON,
            }
        ]
        assert cap.drafts == []
        assert cap.deleted == [(7, Language.PYTHON)]

    def test_failed_result_adds_attempt_and_saves_draft(self, monkeypatch):
        cap = stub_attempt_persistence(monkeypatch)

        modal = make_modal(
            question=FakeQuestion(question_id=7),
            user_code="  broken()  ",
            elapsed=25.5,
            language=Language.RUST,
        )

        modal._save_result(status=RunStatus.FAILED, created_at=1234.5)

        assert cap.attempts == [
            {
                "problem_id": 7,
                "status": RunStatus.FAILED,
                "elapsed": 25.5,
                "created_at": 1234.5,
                "code": "broken()",
                "lang_id": Language.RUST,
            }
        ]
        assert cap.drafts == [
            {
                "problem_id": 7,
                "lang_id": Language.RUST,
                "code": "broken()",
                "elapsed": 25.5,
                "updated_at": 1234.5,
            }
        ]
        assert cap.deleted == []

    @pytest.mark.parametrize(
        "status",
        [
            RunStatus.FAILED,
            RunStatus.COMPILE_ERROR,
            RunStatus.TIMEOUT,
            RunStatus.ERROR,
        ],
    )
    def test_unsuccessful_status_saves_draft_and_no_deletion(self, monkeypatch, status):
        cap = stub_attempt_persistence(monkeypatch)

        modal = make_modal(
            user_code="solution()",
            elapsed=8.0,
            language=Language.PYTHON,
        )

        modal._save_result(status=status, created_at=100.0)

        assert len(cap.attempts) == 1
        assert len(cap.drafts) == 1
        assert cap.deleted == []

    def test_strips_user_code(self, monkeypatch):
        cap = stub_attempt_persistence(monkeypatch)

        modal = make_modal(user_code="\n\n  print('hello')  \n\n")

        modal._save_result(status=RunStatus.FAILED, created_at=100.0)

        assert cap.attempts[0]["code"] == "print('hello')"
        assert cap.drafts[0]["code"] == "print('hello')"


# run_user_code
class TestRunUserCode:
    @pytest.mark.asyncio
    async def test_passes_question_tests_and_saves_passed_result(self, monkeypatch):
        question = FakeQuestion(
            question_id=42,
            tests="assert solution() == 42",
        )
        cap = stub_run_user_code(
            monkeypatch,
            result=ExecutionResult(status=RunStatus.PASSED),
            created_at=1234.5,
        )

        modal = make_modal(question=question, user_code="solution()")
        await modal.run_user_code()

        assert cap.captured["user_code"] == "solution()"
        assert cap.captured["test_code"] == "assert solution() == 42"
        assert cap.captured["language"] is Language.PYTHON
        assert callable(cap.captured["on_line"])
        assert cap.saved == {
            "status": RunStatus.PASSED,
            "created_at": 1234.5,
        }

    @pytest.mark.asyncio
    async def test_shows_compile_error(self, monkeypatch):
        cap = stub_run_user_code(
            monkeypatch,
            result=ExecutionResult(
                status=RunStatus.COMPILE_ERROR,
                stderr="expected `;`",
            ),
        )

        await make_modal().run_user_code()

        assert cap.errors == [("compilation failed", "expected `;`")]
        assert cap.saved["status"] is RunStatus.COMPILE_ERROR
        assert cap.saved["created_at"] == 100.0

    @pytest.mark.asyncio
    async def test_shows_timeout(self, monkeypatch):
        cap = stub_run_user_code(
            monkeypatch,
            result=ExecutionResult(status=RunStatus.TIMEOUT),
        )

        await make_modal().run_user_code()

        assert cap.errors == [
            ("timed out", "your solution must run within 9 seconds."),
        ]

    @pytest.mark.asyncio
    async def test_shows_runtime_error(self, monkeypatch):
        cap = stub_run_user_code(
            monkeypatch,
            result=ExecutionResult(
                status=RunStatus.ERROR,
                stderr="segmentation fault",
            ),
        )

        await make_modal().run_user_code()

        assert cap.errors == [
            ("error running code", "segmentation fault"),
        ]

    @pytest.mark.asyncio
    async def test_shows_success(self, monkeypatch):
        cap = stub_run_user_code(
            monkeypatch,
            result=ExecutionResult(status=RunStatus.PASSED),
        )

        await make_modal().run_user_code()

        assert cap.success_called is True


# Dismissal
class TestDismissal:
    @pytest.mark.asyncio
    async def test_escape_dismisses_modal(self, disable_worker):
        app = HostApp()

        async with app.run_test() as pilot:
            modal = make_modal()

            app.push_screen(modal)
            await pilot.pause()

            assert app.screen is modal

            await pilot.press("escape")
            await pilot.pause()

            assert app.screen is not modal
