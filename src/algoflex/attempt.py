from textual.app import App
from textual.widgets import TextArea, Button, Markdown, Footer
from home import ProblemScreen
from result import ResultModal
from textual.containers import VerticalGroup, HorizontalGroup
from textual.screen import ModalScreen, Screen


class AttemptScreen(Screen):
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
        with HorizontalGroup():
            yield ProblemScreen()
            with VerticalGroup():
                yield TextArea(
                    self.DEFAULT_CODE, show_line_numbers=True, language="python"
                )
                with HorizontalGroup():
                    yield Button("submit")
                    yield Button("cancel")
        yield Footer()

    def action_show_modal(self):
        code = self.query_one(TextArea)
        self.app.push_screen(ResultModal(code.text))


# if __name__ == "__main__":
#     app = AttemptScreen()
#     app.run()
