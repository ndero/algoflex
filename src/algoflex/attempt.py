from textual.app import App
from textual.widgets import TextArea, Footer, TabbedContent
from textual.containers import Horizontal
from textual.screen import Screen
from textual.binding import Binding
from algoflex.custom_widgets import Title, Problem
from algoflex.result import ResultModal
from algoflex.questions import questions
from algoflex.db import get_db
from tinydb import Query
from time import monotonic

KV = Query()


class AttemptScreen(Screen):
    BINDINGS = [
        Binding("s", "submit", "submit", tooltip="submit your solution"),
        Binding("b", "back", "back", tooltip="Go to home"),
    ]
    DEFAULT_CSS = """
    Horizontal {
        Problem {
            margin: 0 1;
            height: 1fr;
        }
    }
    TextArea {
        margin-right: 1;
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
        stats = get_db()
        s = stats.get(KV.problem_id == self.problem_id) or {}
        recent_code, saved_code = s.get("recent_code", ""), s.get("saved_code", "")

        yield Title()
        with Horizontal():
            yield Problem(description)
            with TabbedContent(*["Attempt", "Recent Solution", "Saved Solution"]):
                yield TextArea(
                    code,
                    show_line_numbers=True,
                    language="python",
                    compact=True,
                    tab_behavior="indent",
                )
                yield TextArea(
                    recent_code,
                    show_line_numbers=True,
                    language="python",
                    compact=True,
                    tab_behavior="indent",
                    read_only=True,
                    placeholder="# Recent correct submitted solution will be shown here.",
                )
                yield TextArea(
                    saved_code,
                    show_line_numbers=True,
                    language="python",
                    compact=True,
                    tab_behavior="indent",
                    placeholder="# You can save a solution here for future reference",
                )

        yield Footer()

    def action_submit(self):
        code = self.query_one(TextArea)
        elapsed = monotonic() - self.test_time
        self.app.push_screen(ResultModal(self.problem_id, code.text, elapsed))

    def action_back(self):
        self.dismiss()
