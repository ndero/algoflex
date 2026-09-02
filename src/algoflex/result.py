import time
from typing import ClassVar

from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Footer, RichLog, Static

from algoflex.db import add_attempt, add_draft, delete_draft
from algoflex.questions import questions
from algoflex.runner import run_solution
from algoflex.types import RunStatus
from algoflex.utils import fmt_secs


class ResultModal(ModalScreen):
    BINDINGS: ClassVar = [("escape", "dismiss", "dismiss")]

    SPINNER: ClassVar = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

    DEFAULT_CSS = """
    ResultModal {
        align: center middle;

        & > * {
            max-width: 90;
        }

        RichLog {
            width: 1fr;
            height: auto;
            max-height: 16;
            min-height: 5;
            padding: 0 2;
            padding-top: 1;
            overflow-y: auto;
            background: $boost;
        }

        #status {
            background: $boost;
            padding: 0 2;
        }
    }
    """

    def __init__(self, problem_id, user_code, elapsed, best, language) -> None:
        super().__init__()

        self.problem_id: int = problem_id
        self.user_code: str = user_code
        self.elapsed: float = elapsed
        self.best: float | None = best
        self.language = language

        self._spinner_index = 0
        self._spinner_timer = None

    def compose(self) -> ComposeResult:
        yield RichLog(
            markup=True,
            wrap=True,
            max_lines=1_000,
            auto_scroll=True,
        )
        yield Static(id="status")
        yield Footer()

    def on_mount(self) -> None:
        self._log = self.query_one(RichLog)
        self._status = self.query_one("#status", Static)

        self.run_worker(self.run_user_code())

    async def run_user_code(self) -> None:
        now = time.time()
        question = questions.get(self.problem_id)

        self.start_loading()

        result = await run_solution(
            self.user_code,
            question.tests_for(self.language),
            self.language,
            on_line=self._write_line,
        )

        self.stop_loading()

        if result.status is RunStatus.COMPILE_ERROR:
            self._show_error("compilation failed", result.stderr)

        elif result.status is RunStatus.TIMEOUT:
            self._show_error(
                "timed out",
                "your solution must run within 9 seconds.",
            )

        elif result.status is RunStatus.ERROR:
            self._show_error("error running code", result.stderr)

        elif result.status is RunStatus.PASSED:
            self._show_success()

        self._save_result(status=result.status, created_at=now)

    async def _write_line(self, line: str, is_stderr: bool) -> None:
        if is_stderr:
            self._log.write(f"[red][b]x[/] {line}")
        else:
            self._log.write(line)

    def start_loading(self, message: str = "Running tests...") -> None:
        self._spinner_index = 0
        self._status.update(
            f"{self.SPINNER[0]} {message}",
        )

        self._spinner_timer = self.set_interval(
            0.12,
            lambda: self._update_spinner(message),
        )

    def _update_spinner(self, message: str) -> None:
        self._spinner_index = (self._spinner_index + 1) % len(self.SPINNER)

        self._status.update(
            f"{self.SPINNER[self._spinner_index]} {message}",
        )

    def stop_loading(self) -> None:
        if self._spinner_timer is not None:
            self._spinner_timer.stop()
            self._spinner_timer = None

        if self._status is not None:
            self._status.update("")

    def _show_error(self, title: str, message: str) -> None:
        self._log.write(
            f"[red][b]x[/] {title}\n\t{message}",
        )

    def _show_success(self) -> None:
        if self.best is None or self.elapsed < self.best:
            self._show_new_best()

    def _show_new_best(self) -> None:
        widget = Static(f"[b]New best time!! → {fmt_secs(self.elapsed)}[/]")
        widget.styles.height = 3
        widget.styles.content_align = ("center", "middle")
        widget.styles.background = "#303134"
        self.mount(widget)

    def _save_result(self, *, status: RunStatus, created_at: float) -> None:
        add_attempt(
            {
                "problem_id": self.problem_id,
                "status": status,
                "elapsed": self.elapsed,
                "created_at": created_at,
                "code": self.user_code.strip(),
                "lang_id": self.language,
            }
        )

        if status is RunStatus.PASSED:
            delete_draft(self.problem_id, self.language)
        else:
            add_draft(
                {
                    "problem_id": self.problem_id,
                    "lang_id": self.language,
                    "code": self.user_code.strip(),
                    "elapsed": self.elapsed,
                    "updated_at": created_at,
                },
            )
