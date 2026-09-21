import pytest
from textual.app import App, ComposeResult
from textual.widgets import Markdown, OptionList, Select, Static

from algoflex.custom_widgets import Problem, Title
from algoflex.types import Language


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


@pytest.mark.asyncio
async def test_problem_renders_markdown():
    markdown = "# Two Sum\n\nFind two numbers."

    app = ProblemApp(markdown)

    async with app.run_test():
        problem = app.query_one(Problem)
        markdown_widget = problem.query_one(Markdown)

        assert problem.markdown == markdown
        assert markdown_widget is not None


@pytest.mark.asyncio
async def test_problem_contains_one_markdown_widget():
    app = ProblemApp("# Hello")

    async with app.run_test():
        assert len(app.query(Markdown)) == 1


# Title
@pytest.mark.asyncio
async def test_title_displays_application_title():
    app = TitleApp()

    async with app.run_test():
        title = app.query_one("#title", expect_type=Static)

        rendered = str(title.render())

        assert "Algoflex" in rendered
        assert "terminal code practice app" in rendered


@pytest.mark.asyncio
async def test_title_hides_language_selector_by_default():
    app = TitleApp()

    async with app.run_test():
        assert not app.query("#language-selector")


@pytest.mark.asyncio
async def test_title_hides_language_selector_without_question():
    app = TitleApp(
        show_language_selector=True,
        question=None,
    )

    async with app.run_test():
        assert not app.query("#language-selector")


@pytest.mark.asyncio
async def test_title_displays_language_selector_when_enabled():
    app = TitleApp(
        question=FakeQuestion(),
        show_language_selector=True,
    )

    async with app.run_test():
        selector = app.query_one(
            "#language-selector",
            expect_type=Select,
        )

        assert selector.value == Language.PYTHON


@pytest.mark.asyncio
async def test_title_shows_only_supported_languages():
    question = FakeQuestion(
        languages=[Language.PYTHON],
    )
    app = TitleApp(
        question=question,
        show_language_selector=True,
    )

    async with app.run_test():
        selector = app.query_one(
            "#language-selector",
            expect_type=Select,
        )
        option_list = selector.query_one(OptionList)

        values = {language for language in question.languages}

        assert len(option_list.options) == len(question.languages)
        assert values == {Language.PYTHON}
        assert Language.RUST not in values


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
async def test_title_initializes_supported_selected_language(
    supported_languages,
    selected_language,
):
    app = TitleApp(
        question=FakeQuestion(supported_languages),
        language=selected_language,
        show_language_selector=True,
    )

    async with app.run_test():
        selector = app.query_one(
            "#language-selector",
            expect_type=Select,
        )

        assert selector.value == selected_language


@pytest.mark.asyncio
async def test_title_selector_contains_correct_language_labels():
    question = FakeQuestion(
        languages=[Language.PYTHON, Language.RUST],
    )
    app = TitleApp(
        question=question,
        show_language_selector=True,
    )

    async with app.run_test():
        selector = app.query_one(
            "#language-selector",
            expect_type=Select,
        )
        option_list = selector.query_one(OptionList)

        labels = {str(option.prompt) for option in option_list.options}

        assert labels == {
            Language.PYTHON.label,
            Language.RUST.label,
        }


@pytest.mark.asyncio
async def test_title_single_supported_language():
    question = FakeQuestion(
        languages=[Language.RUST],
    )
    app = TitleApp(
        question=question,
        language=Language.RUST,
        show_language_selector=True,
    )

    async with app.run_test():
        selector = app.query_one(
            "#language-selector",
            expect_type=Select,
        )
        option_list = selector.query_one(OptionList)

        assert len(option_list.options) == 1
        assert option_list.options[0].prompt == Language.RUST.label
        assert selector.value == Language.RUST


@pytest.mark.asyncio
async def test_language_change_reaches_parent_app():
    app = TitleApp(
        question=FakeQuestion(),
        show_language_selector=True,
        language=Language.PYTHON,
    )

    async with app.run_test() as pilot:
        title = app.query_one(Title)
        selector = app.query_one(
            "#language-selector",
            expect_type=Select,
        )

        title.on_select_changed(
            Select.Changed(
                selector,
                Language.RUST,  # type: ignore
            )
        )

        await pilot.pause()

        assert app.changed_language is Language.RUST
