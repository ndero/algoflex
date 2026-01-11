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
stats = get_db()


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
        s = stats.get(KV.problem_id == self.problem_id) or {}
        recent_code, saved_code = s.get("recent_code", ""), s.get("saved_code", "")

        yield Title()
        with Horizontal():
            yield Problem(description)
            with TabbedContent("Attempt", "Recent Solution", "Saved Solution"):
                with Vertical():
                    yield TextArea(
                        code,
                        show_line_numbers=True,
                        language="python",
                        compact=True,
                        tab_behavior="indent",
                    )
                    with Horizontal():
                        yield Button(id="submit", label="Submit", flat=True)
                        yield Button(id="save", label="Save", flat=True)
                yield TextArea(
                    recent_code,
                    show_line_numbers=True,
                    language="python",
                    compact=True,
                    read_only=True,
                    placeholder="# Recent correct submitted solution will be shown here.",
                )
                yield TextArea(
                    saved_code,
                    show_line_numbers=True,
                    language="python",
                    compact=True,
                    read_only=True,
                    placeholder="# Your saved solution will appear here",
                )
        yield Footer()

    @on(Button.Pressed, "#save")
    def save_code(self):
        code = self.query_one(TextArea)
        stats.upsert({"saved_code": code.text}, KV.problem_id == self.problem_id)
        self.notify("Saved - can be accessed in saved solution tab")

    @on(Button.Pressed, "#submit")
    def submit_code(self):
        code = self.query_one(TextArea)
        elapsed = monotonic() - self.test_time
        self.app.push_screen(ResultModal(self.problem_id, code.text, elapsed))

    def action_back(self):
        self.dismiss()
