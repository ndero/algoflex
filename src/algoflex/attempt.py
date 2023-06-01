from textual.app import App
from textual.widgets import TextArea, Button, Markdown, Footer
from home import ProblemScreen, TitleScreen
from result import ResultModal
from textual.containers import Vertical, Horizontal
from textual.screen import ModalScreen, Screen
from textual.binding import Binding


class AttemptScreen(Screen):
    BINDINGS = [Binding("s", "submit", "submit", tooltip="submit your solution")]
    DEFAULT_CSS = """
    ProblemScreen {
        margin: 0 1;
    }
    TextArea {
        margin-right: 1;
    }
    """
    DEFAULT_CODE = """\
def solution(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
"""

    def compose(self):
        yield TitleScreen()
        with Horizontal():
            yield ProblemScreen()
            with Vertical():
                yield TextArea(
                    self.DEFAULT_CODE,
                    show_line_numbers=True,
                    language="python",
                    compact=True,
                    tab_behavior="indent",
                )
        yield Footer()

    def action_submit(self):
        code = self.query_one(TextArea)
        self.app.push_screen(ResultModal(code.text))
