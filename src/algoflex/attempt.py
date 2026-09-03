import sqlite3
from time import monotonic
from typing import ClassVar

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, ScrollableContainer, Vertical
from textual.screen import Screen
from textual.widgets import Footer, Markdown, Static, TabbedContent, TextArea

from algoflex.custom_widgets import Problem, Title
from algoflex.db import get_best_attempts, get_draft, get_recent_attempts
from algoflex.questions import questions
from algoflex.result import ResultModal
from algoflex.types import Language, RunStatus
from algoflex.utils import fmt_secs, time_ago


class AttemptScreen(Screen):
    BINDINGS: ClassVar[list[Binding]] = [
        Binding("ctrl+s", "submit", "submit", tooltip="Submit your solution"),
        Binding(
            "ctrl+l", "maximize", "max/min editor", tooltip="maximize/minimize editor"
        ),
        Binding("ctrl+b", "back", "back", tooltip="Go to home"),
    ]

    DEFAULT_CSS = """
    Horizontal {
        Problem {
            margin: 0 1;
            height: 1fr;
            width: 1fr;
        }
        TabbedContent {
            width: 1fr;
        }
    }

    TextArea {
        margin-right: 1;
    }

    Vertical {
        Horizontal {
            height: 4;
            align: center middle;
            background: $boost;
            border-top: hkey $background;
            margin-right: 1;
        }
    }

    #timeline {
        padding: 1 2;
        border-left: vkey $boost;
    }

    Markdown {
        border-left: vkey $boost;
        height: 1fr;
        overflow-y: auto;
    }
    """

    def __init__(self, problem_id, language, draft):
        super().__init__()
        self.problem_id: int = problem_id
        self.test_time: float = monotonic()
        self.language: Language = language
        self.draft: sqlite3.Row = draft

    def compose(self) -> ComposeResult:
        question = questions.get(self.problem_id)
        description = question.markdown
        code = question.starter_for(self.language)
        if self.draft:
            code = self.draft["code"]

        yield Title(show_language_selector=True, language=self.language)
        with Horizontal():
            yield Problem(description)
            with TabbedContent("Attempt", "Timeline", "Past solutions", id="editor"):
                with Vertical():
                    yield TextArea(
                        code,
                        id="code",
                        show_line_numbers=True,
                        language=self.language.slug,
                        compact=True,
                        tab_behavior="indent",
                    )
                yield ScrollableContainer(Static(id="timeline"))
                yield Markdown(id="solutions")
        yield Footer()

    def on_mount(self) -> None:
        self.best: float | None = None
        self.timeline = self.query_one("#timeline", Static)
        self.solutions = self.query_one("#solutions", Markdown)
        self.editor = self.query_one("#code", TextArea)

        self.update_attempt_view()

    def update_attempt_view(self) -> None:
        """Update attempt timeline and past solutions"""
        attempts = get_recent_attempts(n=-1, problem_id=self.problem_id)
        timeline = self.get_timeline(attempts)
        solutions = self.get_solutions(attempts)

        self.timeline.update(timeline)
        self.solutions.update(solutions)

    def get_timeline(self, attempts) -> str:
        """Display timeline for all language attempts"""
        md = ""
        best_attempts = get_best_attempts(n=1, problem_id=self.problem_id)
        best_attempt = best_attempts[0] if best_attempts else None

        if best_attempt:
            self.best = best_attempt["elapsed"]

        for attempt in attempts:
            md += f"\n|- {RunStatus(attempt['status']).icon} {time_ago(attempt['created_at'])}   \t({fmt_secs(attempt['elapsed'])}) "
            md += Language(attempt["lang_id"]).icon
            if best_attempt and best_attempt["attempt_id"] == attempt["attempt_id"]:
                md += "\t<--- best"
            md += "\n|"

        return md.rstrip("|")

    def get_solutions(self, attempts) -> str:
        """Display all language solutions"""
        md = ""

        for attempt in attempts:
            if RunStatus(attempt["status"]) is RunStatus.PASSED:
                language = Language(attempt["lang_id"])

                md += f"### {time_ago(attempt['created_at'])}\t"
                md += language.icon
                md += f"\n```{language.slug}\n{attempt['code']}\n```\n"

        return md

    def submit(self) -> None:
        def update(_id):
            self.update_attempt_view()

        code = self.query_one("#code", TextArea)
        elapsed_before = self.draft["elapsed"] if self.draft else 0
        elapsed = (monotonic() - self.test_time) + elapsed_before
        self.app.push_screen(
            ResultModal(
                self.problem_id,
                code.text,
                elapsed,
                self.best,
                self.language,
            ),
            update,
        )

    def load_draft(self) -> sqlite3.Row:
        return get_draft(problem_id=self.problem_id, lang_id=self.language)

    def action_back(self) -> None:
        self.dismiss()

    def action_submit(self) -> None:
        self.submit()

    def action_maximize(self) -> None:
        editor = self.query_one("#editor", TabbedContent)
        if not editor.is_maximized:
            self.maximize(editor)
        else:
            self.minimize()

    def on_title_language_changed(self, message: Title.LanguageChanged) -> None:
        if message.language != self.language:
            self.update_language(message.language)

    def update_language(self, language: Language) -> None:
        self.language = language
        question, self.draft = questions.get(self.problem_id), self.load_draft()
        code = question.starter_for(language)
        self.editor.text = self.draft["code"] if self.draft else code
        self.editor.language = language.slug
