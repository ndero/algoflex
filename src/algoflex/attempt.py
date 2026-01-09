from textual.app import App
from textual.widgets import TextArea, Markdown, Footer
from textual.containers import Horizontal
from textual.screen import Screen
from textual.binding import Binding
from algoflex.custom_widgets import Title, Problem
from algoflex.result import ResultModal
from algoflex.questions import questions
from time import monotonic


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
        yield Title()
        with Horizontal():
            yield Problem(description)
            yield TextArea(
                code,
                show_line_numbers=True,
                language="python",
                compact=True,
                tab_behavior="indent",
            )
        yield Footer()

    def action_submit(self):
        code = self.query_one(TextArea)
        elapsed = monotonic() - self.test_time
        self.app.push_screen(ResultModal(self.problem_id, code.text, elapsed))

    def action_back(self):
        self.dismiss()
