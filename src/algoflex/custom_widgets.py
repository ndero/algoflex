from textual.app import ComposeResult
from textual.containers import Container, VerticalScroll
from textual.message import Message
from textual.widgets import Markdown, Select, Static

from algoflex.types import Language


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
        self.markdown = markdown
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Markdown(self.markdown)


class Title(Container):
    class LanguageChanged(Message):
        def __init__(self, language: Language) -> None:
            self.language = language
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

    def __init__(
        self, show_language_selector: bool = False, language: Language = Language.PYTHON
    ) -> None:
        self.show_language_selector = show_language_selector
        self.language = language
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Static(
            "[b]Algoflex - The terminal code practice app[/]",
            id="title",
        )

        if self.show_language_selector:
            yield Select(
                [(language.label, language) for language in Language],
                value=self.language,
                allow_blank=False,
                compact=True,
                id="language-selector",
            )

    def on_select_changed(self, event: Select.Changed) -> None:
        language = Language(event.value)
        self.post_message(message=self.LanguageChanged(language))
