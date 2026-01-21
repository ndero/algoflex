from textual import on
from textual.app import App
from textual.widgets import TextArea, Footer, TabbedContent, Button
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.binding import Binding
from algoflex.custom_widgets import Title, Problem
from algoflex.result import ResultModal
from algoflex.questions import questions
from algoflex.db import get_db
from tinydb import Query
from time import monotonic

KV = Query()
attempts = get_db()


class AttemptScreen(Screen):
    BINDINGS = [
        Binding("b", "back", "back", tooltip="Go to home"),
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
    """

    def __init__(self, problem_id):
        super().__init__()
        self.problem_id = problem_id
        self.test_time = monotonic()

    def compose(self):
        question = questions.get(self.problem_id, {})
        description = question.get("markdown", "")
        code = question.get("code", "")
        passed_attempts = attempts.search(
            (KV.problem_id == self.problem_id) & (KV.passed == True)
        )
        recent_code = "\n\n".join(doc.get("code", "") for doc in passed_attempts)

        yield Title()
        with Horizontal():
            yield Problem(description)
            with TabbedContent("Attempt", "Recent Solution"):
                with Vertical():
                    yield TextArea(
                        code,
                        id="code",
                        show_line_numbers=True,
                        language="python",
                        compact=True,
                        tab_behavior="indent",
                    )
                    with Horizontal():
                        yield Button(id="submit", label="Submit", flat=True)
                yield TextArea(
                    recent_code,
                    show_line_numbers=True,
                    language="python",
                    compact=True,
                    read_only=True,
                    placeholder="# Recent correct submitted solution will be shown here.",
                )
        yield Footer()

    @on(Button.Pressed, "#submit")
    def submit_code(self):
        code = self.query_one("#code", TextArea)
        elapsed = monotonic() - self.test_time
        self.app.push_screen(ResultModal(self.problem_id, code.text, elapsed))

    def action_back(self):
        self.dismiss()
