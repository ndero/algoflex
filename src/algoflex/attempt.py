from textual.app import App
from textual.widgets import TextArea, Button
from home import ProblemScreen
from textual.containers import VerticalGroup, HorizontalGroup
from textual.screen import ModalScreen


class PassScreen(ModalScreen):
    pass


class AttemptScreen(App):
    DEFAULT_TEXT = """\
def solution():
    # your solution here
"""

    def compose(self):
        with HorizontalGroup():
            yield ProblemScreen()
            with VerticalGroup():
                yield TextArea(
                    self.DEFAULT_TEXT, show_line_numbers=True, language="python"
                )
                with HorizontalGroup():
                    yield Button("submit")
                    yield Button("cancel")


if __name__ == "__main__":
    app = AttemptScreen()
    app.run()
