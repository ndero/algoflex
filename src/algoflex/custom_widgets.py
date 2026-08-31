from textual.app import ComposeResult
from textual.containers import Container, VerticalScroll
from textual.message import Message
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

    def __init__(self, markdown) -> None:
        super().__init__()
        self.markdown = markdown

    def compose(self) -> ComposeResult:
        yield Markdown(self.markdown)


class Title(Container):
    class LanguageChanged(Message):
        def __init__(self, lang_id: int) -> None:
            self.lang_id = lang_id
            super().__init__()

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

    def __init__(self, show_language_selector: bool = False, lang_id: int = 1) -> None:
        self.show_language_selector = show_language_selector
        self.lang_id = lang_id
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Static(
            "[b]Algoflex - The terminal code practice app[/]",
            id="title",
        )

        if self.show_language_selector:
            yield Select(
                [
                    ("Python", 1),
                    ("Rust", 2),
                ],
                value=self.lang_id,
                allow_blank=False,
                compact=True,
                id="language-selector",
            )

    def on_select_changed(self, event: Select.Changed) -> None:
        if type(event.value) is int:  # never blank and always an integer
            self.post_message(message=self.LanguageChanged(event.value))
