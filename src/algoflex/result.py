import asyncio
import os
import sys
import tempfile
import time
from pathlib import Path
from typing import ClassVar

from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Footer, RichLog, Static

from algoflex.db import add_attempt, add_draft, delete_draft
from algoflex.questions import questions
from algoflex.utils import fmt_secs


class ResultModal(ModalScreen):
    BINDINGS: ClassVar = [("escape", "dismiss", "dismiss")]
    SPINNER: ClassVar = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    DEFAULT_CSS = """
    ResultModal {
        &>* {
            max-width: 90;
        }
        align: center middle;

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

    def __init__(self, problem_id, user_code, elapsed, best, lang_id):
        super().__init__()
        self.problem_id: int = problem_id
        self.user_code: str = user_code
        self.elapsed: float = elapsed
        self.best: float | None = best
        self.lang_id: int = lang_id

    def on_mount(self) -> None:
        asyncio.create_task(self.run_user_code())
        self.spinner_index = 0
        self.spinner_timer = None

    def start_loading(self, message: str = "Running tests...") -> None:
        status = self.query_one("#status", Static)

        self.spinner_index = 0
        status.update(f"{self.SPINNER[0]} {message}")

        self.spinner_timer = self.set_interval(
            0.08,
            lambda: self._update_spinner(message),
        )

    def _update_spinner(self, message: str) -> None:
        self.spinner_index = (self.spinner_index + 1) % len(self.SPINNER)

        self.query_one("#status", Static).update(
            f"{self.SPINNER[self.spinner_index]} {message}"
        )

    def stop_loading(self) -> None:
        if self.spinner_timer:
            self.spinner_timer.stop()
            self.spinner_timer = None

        self.query_one("#status", Static).update("")

    def compose(self) -> ComposeResult:
        yield RichLog(markup=True, wrap=True, max_lines=1_000, auto_scroll=True)
        yield Static(id="status")
        yield Footer()

    async def run_user_code(self) -> None:
        now = time.time()
        passed = False

        output_log = self.query_one(RichLog)
        user_code = self.user_code.strip()

        question = questions.get(self.problem_id)
        test_code, suffix = question.python_tests, ".py"

        if self.lang_id == 2:  # rust
            test_code = question.rust_tests
            suffix = ".rs"

        full_code = f"{user_code}\n\n{test_code}"
        tmp_path = executable_path = None

        try:
            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=suffix,
                mode="w",
                encoding="utf-8",
            ) as f:
                f.write(full_code)
                tmp_path = f.name

            run_args = [sys.executable, "-u", tmp_path]

            if self.lang_id == 2:
                # compile rust source
                executable_path = tmp_path.removesuffix(".rs")
                compile_args = [
                    "rustc",
                    "--edition",
                    "2024",
                    "-O",
                    tmp_path,
                    "-o",
                    executable_path,
                ]

                compile_proc = await asyncio.create_subprocess_exec(
                    *compile_args,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE,
                )
                _, stderr = await compile_proc.communicate()

                if compile_proc.returncode != 0:
                    output_log.write("[red][b]x[/][/] compilation failed")
                    if stderr:
                        for line in stderr.decode().splitlines():
                            output_log.write(
                                f"[red][b]x[/][/] {line}",
                                animate=True,
                            )
                    return

                run_args = [executable_path]

            # run the code
            proc = await asyncio.create_subprocess_exec(
                *run_args,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            async def stream(pipe, is_err=False):
                while True:
                    line = await pipe.readline()
                    if not line:
                        break
                    text = line.decode().rstrip()
                    if is_err:
                        output_log.write(f"[red][b]x[/][/] {text}", animate=True)
                    else:
                        output_log.write(text, animate=True)

            # stream output with timeout
            try:
                self.start_loading("running test...")
                await asyncio.wait_for(
                    asyncio.gather(
                        stream(proc.stdout),
                        stream(proc.stderr, is_err=True),
                    ),
                    timeout=9,
                )
            except TimeoutError:
                proc.kill()
                await proc.wait()
                output_log.write(
                    "[red][b]x[/][/] timed out\tyour solution must run within 9 seconds."
                )
                return
            finally:
                self.stop_loading()

            rc = await proc.wait()

            if rc == 0:
                passed = True
                if not self.best or self.elapsed < self.best:
                    self.new_best()

        except Exception as e:  # noqa: BLE001
            output_log.write(f"[red][b]x[/][/] error running code\n\t{e}", animate=True)

        finally:
            if tmp_path and Path(tmp_path).exists():
                os.remove(tmp_path)

            if executable_path and Path(executable_path).exists():
                os.remove(executable_path)

            add_attempt(
                {
                    "problem_id": self.problem_id,
                    "passed": passed,
                    "elapsed": self.elapsed,
                    "created_at": now,
                    "code": user_code,
                    "lang_id": self.lang_id,
                }
            )

            if passed:
                delete_draft(self.problem_id, self.lang_id)
            else:
                add_draft(
                    {
                        "problem_id": self.problem_id,
                        "lang_id": self.lang_id,
                        "code": user_code,
                        "elapsed": self.elapsed,
                        "updated_at": now,
                    }
                )

    def new_best(self) -> None:
        widget = Static(f"[b]New best time!! --> {fmt_secs(self.elapsed)}[/]")
        widget.styles.height = 3
        widget.styles.content_align = ("center", "middle")
        widget.styles.background = "#303134"
        self.mount(widget)
