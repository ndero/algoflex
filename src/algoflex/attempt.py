from time import monotonic
from typing import ClassVar

from textual.binding import Binding
from textual.containers import Horizontal, ScrollableContainer, Vertical
from textual.screen import Screen
from textual.widgets import Footer, Markdown, Static, TabbedContent, TextArea

from algoflex.custom_widgets import Problem, Title
from algoflex.db import get_attempts, get_draft
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
        self.elapsed_before = 0
        self.best = None

    def compose(self):
        question = questions.get(self.problem_id)
        description = question.markdown
        code = question.python_starter

        yield Title(show_language_selector=True)
        with Horizontal():
            yield Problem(description)
            with TabbedContent("Attempt", "Timeline", "Past solutions", id="editor"):
                with Vertical():
                    yield TextArea(
                        code,
                        id="code",
                        show_line_numbers=True,
                        language="python",
                        compact=True,
                        tab_behavior="indent",
                    )
                yield ScrollableContainer(Static(id="timeline"))
                yield Markdown(id="solutions")
        yield Footer()

    def on_mount(self):
        self._load_draft()
        self.update()

    def update(self):
        docs = get_attempts(problem_id=self.problem_id, lang_id=1)
        self.update_timeline(docs)
        self.update_solutions(docs)

    def attempt(self):
        def update(_id):
            self.update()

        code = self.query_one("#code", TextArea)
        elapsed = (monotonic() - self.test_time) + self.elapsed_before
        self.app.push_screen(
            ResultModal(self.problem_id, code.text, elapsed, self.best), update
        )

    def update_timeline(self, docs):
        md = ""
        timeline = sorted(docs, key=lambda x: x["created_at"], reverse=True)
        elapsed = [doc["elapsed"] for doc in docs if doc["passed"]]
        self.best = min(elapsed) if elapsed else None
        for doc in timeline:
            md += f"\n|- {('🟢' if doc['passed'] else '🔴')} {time_ago(doc['created_at'])}   \t({fmt_secs(doc['elapsed'])}) 🐍"
            if doc["passed"] and doc["elapsed"] == self.best:
                md += "\t<--- best"
            md += "\n|"
        self.query_one("#timeline", Static).update(md.rstrip("|"))

    def update_solutions(self, docs):
        passed = sorted(
            (doc for doc in docs if doc["passed"]),
            key=lambda x: x["created_at"],
            reverse=True,
        )
        md = ""
        for doc in passed:
            md += f"### {time_ago(doc['created_at'])}\n```python\n{doc['code']}\n```\n"
        self.query_one("#solutions", Markdown).update(md)

    def _load_draft(self):
        draft = get_draft(problem_id=self.problem_id, lang_id=1)
        if draft:
            self.query_one("#code", TextArea).text = draft["code"]
            self.elapsed_before = draft["elapsed"]

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
