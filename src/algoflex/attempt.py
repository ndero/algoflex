from textual.app import App
from textual.widgets import TextArea, Button, Markdown, Footer
from home import ProblemScreen
from textual.containers import VerticalGroup, HorizontalGroup
from textual.screen import ModalScreen, Screen


class PassScreen(ModalScreen):
    PASS_MD = """
    Passed in 12 minutes and 16 seconds!
    Awesome!!
    """
    BINDINGS = [("escape", "dismiss", "Dismiss")]

    DEFAULT_CSS = """
    PassScreen {
        align: center middle;
    }
    Markdown {
        width: 45;
    }
    """

    def compose(self):
        yield Markdown(self.PASS_MD)


class FailScreen(ModalScreen):
    FAIL_MD = """
    Failed,
    """
    BINDINGS = [("escape", "dismiss", "Dismiss")]
    DEFAULT_CSS = """
    FailScreen {
        align: center middle;
    }
    Markdown {
        width: 50;
    }
    """

    def compose(self):
        yield Markdown(self.FAIL_MD)


class AttemptScreen(Screen):
    DEFAULT_TEXT = """\
def solution():
    # your solution here
"""
    BINDINGS = [("s", "show_modal", "Editor")]

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
        yield Footer()

    def action_show_modal(self):
        self.app.push_screen(PassScreen())


# if __name__ == "__main__":
#     app = AttemptScreen()
#     app.run()
