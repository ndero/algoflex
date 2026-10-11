import pytest
from textual.app import App, ComposeResult
from textual.widgets import Markdown, OptionList, Select, Static

from algoflex.custom_widgets import Problem, Title
from algoflex.types import Language


# Test doubles and helper apps
class FakeQuestion:
    def __init__(
        self,
        languages: list[Language] | None = None,
    ) -> None:
        self.languages = (
            languages if languages is not None else [Language.PYTHON, Language.RUST]
        )


class ProblemApp(App):
    def __init__(self, markdown: str) -> None:
        self.markdown = markdown
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Problem(self.markdown)


class TitleApp(App):
    def __init__(
        self,
        *,
        question: FakeQuestion | None = None,
        language: Language = Language.PYTHON,
        show_language_selector: bool = False,
    ) -> None:
        self.question = question
        self.language = language
        self.show_language_selector = show_language_selector
        self.changed_language: Language | None = None
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Title(
            question=self.question,  # type: ignore
            language=self.language,
            show_language_selector=self.show_language_selector,
        )

    def on_title_language_changed(
        self,
        event: Title.LanguageChanged,
    ) -> None:
        self.changed_language = event.language


# Shared helpers
def get_selector(app: App) -> Select:
    """Return the language selector Select from a running TitleApp."""
    return app.query_one("#language-selector", expect_type=Select)


def get_selector_options(app: App) -> OptionList:
    """Return the OptionList inside the language selector."""
    return get_selector(app).query_one(OptionList)


# Problem widget
class TestProblem:
    @pytest.mark.asyncio
    async def test_renders_markdown(self):
        markdown = "# Two Sum\n\nFind two numbers."
        app = ProblemApp(markdown)

        async with app.run_test():
            problem = app.query_one(Problem)
            assert problem.markdown == markdown

    @pytest.mark.asyncio
    async def test_contains_one_markdown_widget(self):
        app = ProblemApp("# Hello")

        async with app.run_test():
            assert len(app.query(Markdown)) == 1


# Title header
class TestTitleHeader:
    @pytest.mark.asyncio
    async def test_displays_application_title(self):
        app = TitleApp()

        async with app.run_test():
            rendered = str(app.query_one("#title", expect_type=Static).render())

            assert "Algoflex" in rendered
            assert "terminal code practice app" in rendered

    @pytest.mark.asyncio
    async def test_hides_language_selector_by_default(self):
        app = TitleApp()

        async with app.run_test():
            assert not app.query("#language-selector")

    @pytest.mark.asyncio
    async def test_hides_language_selector_without_question(self):
        app = TitleApp(show_language_selector=True, question=None)

        async with app.run_test():
            assert not app.query("#language-selector")


# Language selector
class TestLanguageSelector:
    @pytest.mark.asyncio
    async def test_displays_when_enabled(self):
        app = TitleApp(
            question=FakeQuestion(),
            show_language_selector=True,
        )

        async with app.run_test():
            assert get_selector(app).value == Language.PYTHON

    @pytest.mark.asyncio
    async def test_shows_only_supported_languages(self):
        question = FakeQuestion(languages=[Language.PYTHON])
        app = TitleApp(question=question, show_language_selector=True)

        async with app.run_test():
            options = get_selector_options(app)

            prompts = {str(option.prompt) for option in options.options}

            assert len(options.options) == len(question.languages)
            assert prompts == {Language.PYTHON.label}

    @pytest.mark.parametrize(
        ("supported_languages", "selected_language"),
        [
            ([Language.PYTHON, Language.RUST], Language.PYTHON),
            ([Language.PYTHON, Language.RUST], Language.RUST),
            ([Language.PYTHON], Language.PYTHON),
            ([Language.RUST], Language.RUST),
        ],
    )
    @pytest.mark.asyncio
    async def test_initializes_to_supported_selected_language(
        self,
        supported_languages,
        selected_language,
    ):
        app = TitleApp(
            question=FakeQuestion(supported_languages),
            language=selected_language,
            show_language_selector=True,
        )

        async with app.run_test():
            assert get_selector(app).value == selected_language

    @pytest.mark.asyncio
    async def test_contains_correct_language_labels(self):
        question = FakeQuestion(languages=[Language.PYTHON, Language.RUST])
        app = TitleApp(
            question=question,
            show_language_selector=True,
        )

        async with app.run_test():
            options = get_selector_options(app)

            labels = {str(option.prompt) for option in options.options}

            assert labels == {
                Language.PYTHON.label,
                Language.RUST.label,
            }

    @pytest.mark.asyncio
    async def test_single_supported_language(self):
        question = FakeQuestion(languages=[Language.RUST])
        app = TitleApp(
            question=question,
            language=Language.RUST,
            show_language_selector=True,
        )

        async with app.run_test():
            options = get_selector_options(app)
            selector = get_selector(app)

            assert len(options.options) == 1
            assert options.options[0].prompt == Language.RUST.label
            assert selector.value == Language.RUST


# Language change events
class TestLanguageChangedEvent:
    @pytest.mark.asyncio
    async def test_reaches_parent_app(self):
        app = TitleApp(
            question=FakeQuestion(),
            show_language_selector=True,
            language=Language.PYTHON,
        )

        async with app.run_test() as pilot:
            get_selector(app).value = Language.RUST
            await pilot.pause()

            assert app.changed_language is Language.RUST
