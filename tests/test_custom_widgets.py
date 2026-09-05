import pytest
from textual.app import App, ComposeResult
from textual.widgets import Markdown, Select, Static

from algoflex.custom_widgets import Problem, Title
from algoflex.types import Language


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
        show_language_selector: bool = False,
        language: Language = Language.PYTHON,
    ) -> None:
        self.show_language_selector = show_language_selector
        self.language = language
        self.changed_language: Language | None = None
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Title(
            show_language_selector=self.show_language_selector,
            language=self.language,
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
async def test_title_displays_language_selector_when_enabled():
    app = TitleApp(show_language_selector=True)

    async with app.run_test():
        selector = app.query_one(
            "#language-selector",
            expect_type=Select,
        )

        assert selector.value == Language.PYTHON


@pytest.mark.parametrize("language", list(Language))
@pytest.mark.asyncio
async def test_title_initializes_selected_language(language):
    app = TitleApp(
        show_language_selector=True,
        language=language,
    )

    async with app.run_test():
        selector = app.query_one(
            "#language-selector",
            expect_type=Select,
        )

        assert selector.value == language


@pytest.mark.asyncio
async def test_language_change_reaches_parent_app():
    app = TitleApp(
        show_language_selector=True,
        language=Language.PYTHON,
    )

    async with app.run_test() as pilot:
        title = app.query_one(Title)
        selector = app.query_one(
            "#language-selector",
            expect_type=Select,
        )

        target = next(
            language for language in Language if language is not Language.PYTHON
        )

        title.on_select_changed(
            Select.Changed(
                selector,
                target,
            )
        )

        await pilot.pause()

        assert app.changed_language is target
