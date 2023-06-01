from textual.app import App
from textual.widgets import TextArea, Button, Markdown, Footer
from home import ProblemScreen, TitleScreen
from result import ResultModal
from textual.containers import Vertical, Horizontal
from textual.screen import ModalScreen, Screen


class AttemptScreen(Screen):
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
    BINDINGS = [("s", "show_modal", "Editor")]

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
                )
        yield Footer()

    def action_show_modal(self):
        code = self.query_one(TextArea)
        self.app.push_screen(ResultModal(code.text))
