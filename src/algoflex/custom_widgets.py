from textual.containers import Container, VerticalScroll
from textual.widgets import Markdown, Select, Static


class Problem(VerticalScroll):
    DEFAULT_CSS = """
    VerticalScroll {
        Markdown {
            height: 1fr;
            padding: 0 1;
        }
    }
    """

    def __init__(self, problem):
        super().__init__()
        self.problem = problem

    def compose(self):
        yield Markdown(self.problem)


class Title(Container):
    DEFAULT_CSS = """
    Title {
        height: 3;
        background: $boost;
    }

    #title {
        width: 1fr;
        height: 1fr;
        color: $markdown-h1-color;
        content-align: center middle;
    }

    #language-selector {
        dock: right;
        width: 16;
        height: 1fr;
        margin-right: 1;
        box-sizing: content-box;
        background: black;

        SelectCurrent {
            padding-left: 1;
        }

        & > SelectOverlay {
            padding: 1;
            background: black;
        }
    }
    """

    def __init__(self, show_language_selector: bool = False):
        super().__init__()
        self.show_language_selector = show_language_selector

    def compose(self):
        yield Static(
            "[b]Algoflex - The terminal code practice app[/]",
            id="title",
        )

        if self.show_language_selector:
            yield Select.from_values(
                ["python", "rust"],
                allow_blank=False,
                compact=True,
                id="language-selector",
            )
