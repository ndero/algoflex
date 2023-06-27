from textual.containers import VerticalScroll, Center
from textual.widgets import Markdown, Static


class ProblemScreen(VerticalScroll):
    DEFAULT_CSS = """
    VerticalScroll {
        Markdown {
            height: 100%;
            padding: 0 1;
        }
    }
    """

    def __init__(self, problem):
        super().__init__()
        self.problem = problem

    def compose(self):
        with VerticalScroll():
            yield Markdown(markdown=self.problem)


class TitleScreen(Center):
    DEFAULT_CSS = """
    TitleScreen {
        height: 3;
        Static {
            height: 100%;
            color: $markdown-h1-color;
            background: $boost;
            content-align: center middle;
        }
    }
    """

    def compose(self):
        yield Static("[b]Algoflex - The terminal code practice app[/]")
