from time import monotonic
from typing import ClassVar

from textual.binding import Binding
from textual.containers import Horizontal, ScrollableContainer, Vertical
from textual.screen import Screen
from textual.widgets import Footer, Markdown, Static, TabbedContent, TextArea

from algoflex.custom_widgets import Problem, Title
from algoflex.db import get_attempts, get_draft, get_latest_attempt
from algoflex.questions import questions
from algoflex.result import ResultModal
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

    def __init__(self, problem_id):
        super().__init__()
        self.problem_id = problem_id
        self.test_time = monotonic()
        self.best = None

        recent_attempt = get_latest_attempt()
        self.language = (
            "rust" if recent_attempt and recent_attempt["lang_id"] == 2 else "python"
        )
        self.draft = self.load_draft()

    def compose(self):
        question = questions.get(self.problem_id)
        description = question.markdown

        code = (
            question.python_starter
            if self.language == "python"
            else question.rust_starter
        )

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
                        language=self.language,
                        compact=True,
                        tab_behavior="indent",
                    )
                yield ScrollableContainer(Static(id="timeline"))
                yield Markdown(id="solutions")
        yield Footer()

    def on_mount(self):
        self.update()

    def update(self):
        """Update attempt timeline and past solutions"""
        attempts = get_attempts(problem_id=self.problem_id)
        self.update_timeline(attempts)
        self.update_solutions(attempts)

    def attempt(self):
        def update(_id):
            self.update()

        code = self.query_one("#code", TextArea)
        elapsed_before = self.draft["elapsed"] if self.draft else 0
        elapsed = (monotonic() - self.test_time) + elapsed_before
        self.app.push_screen(
            ResultModal(self.problem_id, code.text, elapsed, self.best, self.language),
            update,
        )

    def update_timeline(self, attempts):
        """Display timeline for all language attempts"""
        md = ""
        timeline = sorted(attempts, key=lambda x: x["created_at"], reverse=True)
        elapsed = [attempt["elapsed"] for attempt in attempts if attempt["passed"]]
        self.best = min(elapsed) if elapsed else None
        for attempt in timeline:
            md += f"\n|- {('🟢' if attempt['passed'] else '🔴')} {time_ago(attempt['created_at'])}   \t({fmt_secs(attempt['elapsed'])}) "
            md += "🐍" if attempt["lang_id"] == 1 else "🦀"
            if attempt["passed"] and attempt["elapsed"] == self.best:
                md += "\t<--- best"
            md += "\n|"
        self.query_one("#timeline", Static).update(md.rstrip("|"))

    def update_solutions(self, attempts):
        """Display all language solutions"""
        passed = sorted(
            (attempt for attempt in attempts if attempt["passed"]),
            key=lambda x: x["created_at"],
            reverse=True,
        )
        md = ""
        for attempt in passed:
            lang = "python" if attempt["lang_id"] == 1 else "rust"
            md += f"### {time_ago(attempt['created_at'])}\n```{lang}\n{attempt['code']}\n```\n"
        self.query_one("#solutions", Markdown).update(md)

    def load_draft(self):
        lang_id = 2 if self.language == "rust" else 1
        return get_draft(problem_id=self.problem_id, lang_id=lang_id)

    def action_back(self):
        self.dismiss()

    def action_submit(self):
        self.attempt()

    def action_maximize(self) -> None:
        editor = self.query_one("#editor", TabbedContent)
        if not editor.is_maximized:
            self.maximize(editor)
        else:
            self.minimize()

    def on_title_language_changed(self, message: Title.LanguageChanged) -> None:
        if message.language != self.language:
            self.update_language(message.language)

    def update_language(self, language: str) -> None:
        editor = self.query_one("#code", TextArea)
        self.language = language
        question, draft = questions.get(self.problem_id), self.load_draft()
        code = (
            question.python_starter if language == "python" else question.rust_starter
        )

        editor.text, editor.language = draft["code"] if draft else code, language
