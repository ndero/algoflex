from typing import ClassVar

import pytest
from textual.app import App
from textual.widgets import Input, Label, ListView

from algoflex import search
from algoflex.search import SearchScreen


class FakeQuestion:
    def __init__(self, title: str) -> None:
        self.title = title


class FakeQuestions:
    ids: ClassVar = [1, 2, 3, 4]

    def __init__(self) -> None:
        self._questions = {
            1: FakeQuestion("Two Sum"),
            2: FakeQuestion("Valid Parentheses"),
            3: FakeQuestion("Binary Search"),
            4: FakeQuestion("Merge Intervals"),
        }

    def get(self, problem_id: int) -> FakeQuestion:
        return self._questions[problem_id]


class SearchApp(App):
    def __init__(self) -> None:
        self.result: int | None = None
        super().__init__()

    def on_mount(self) -> None:
        self.push_screen(
            SearchScreen(),
            callback=self._on_result,
        )

    def _on_result(self, result: int | None) -> None:
        self.result = result


@pytest.fixture
def fake_questions(monkeypatch):
    questions = FakeQuestions()
    monkeypatch.setattr(search, "questions", questions)
    return questions


@pytest.fixture
def passed_problem_ids(monkeypatch):
    passed = {2}
    monkeypatch.setattr(search, "get_passed_problem_ids", lambda: passed)
    return passed


@pytest.fixture
def search_app(fake_questions, passed_problem_ids):
    return SearchApp()


@pytest.mark.asyncio
async def test_search_screen_composes_search_input_and_results(search_app):
    async with search_app.run_test():
        assert search_app.screen.query_one("#search", Input)
        assert search_app.screen.query_one("#results", ListView)


@pytest.mark.asyncio
async def test_search_input_has_expected_placeholder(search_app):
    async with search_app.run_test():
        search_input = search_app.screen.query_one("#search", Input)

        assert search_input.placeholder == "Search problems..."


@pytest.mark.asyncio
async def test_search_screen_loads_all_problems(
    search_app,
    fake_questions,
    passed_problem_ids,
):
    async with search_app.run_test():
        screen = search_app.screen
        results = screen.query_one("#results", ListView)

        assert len(screen.problems) == 4
        assert len(results.children) == 4


@pytest.mark.asyncio
async def test_search_screen_builds_problem_data(
    search_app,
    fake_questions,
    passed_problem_ids,
):
    async with search_app.run_test():
        assert search_app.screen.problems == [
            (" ", 1, "Two Sum"),
            ("✓", 2, "Valid Parentheses"),
            (" ", 3, "Binary Search"),
            (" ", 4, "Merge Intervals"),
        ]


@pytest.mark.asyncio
async def test_passed_problem_is_marked(
    search_app,
    fake_questions,
    passed_problem_ids,
):
    async with search_app.run_test():
        results = search_app.screen.query_one("#results", ListView)
        labels = list(results.query(Label))

        assert len(labels) == 4
        assert str(labels[0].render()).startswith(" ")
        assert str(labels[1].render()).startswith("✓")


@pytest.mark.asyncio
async def test_each_result_uses_problem_id_as_widget_id(
    search_app,
    fake_questions,
    passed_problem_ids,
):
    async with search_app.run_test():
        results = search_app.screen.query_one("#results", ListView)

        assert [item.id for item in results.children] == [
            "item-1",
            "item-2",
            "item-3",
            "item-4",
        ]


@pytest.mark.asyncio
async def test_search_filters_by_title(
    search_app,
    fake_questions,
    passed_problem_ids,
):
    async with search_app.run_test() as pilot:
        search_input = search_app.screen.query_one("#search", Input)

        search_input.value = "binary"
        await pilot.pause()

        results = search_app.screen.query_one("#results", ListView)

        assert len(results.children) == 1
        assert results.children[0].id == "item-3"


@pytest.mark.asyncio
async def test_search_is_case_insensitive(
    search_app,
    fake_questions,
    passed_problem_ids,
):
    async with search_app.run_test() as pilot:
        search_input = search_app.screen.query_one("#search", Input)

        search_input.value = "VALID PARENTHESES"
        await pilot.pause()

        results = search_app.screen.query_one("#results", ListView)

        assert len(results.children) == 1
        assert results.children[0].id == "item-2"


@pytest.mark.asyncio
async def test_search_strips_leading_and_trailing_whitespace(
    search_app,
    fake_questions,
    passed_problem_ids,
):
    async with search_app.run_test() as pilot:
        search_input = search_app.screen.query_one("#search", Input)

        search_input.value = "   two sum   "
        await pilot.pause()

        results = search_app.screen.query_one("#results", ListView)

        assert len(results.children) == 1
        assert results.children[0].id == "item-1"


@pytest.mark.asyncio
async def test_search_matches_partial_title(
    search_app,
    fake_questions,
    passed_problem_ids,
):
    async with search_app.run_test() as pilot:
        search_input = search_app.screen.query_one("#search", Input)

        search_input.value = "search"
        await pilot.pause()

        results = search_app.screen.query_one("#results", ListView)

        assert len(results.children) == 1
        assert results.children[0].id == "item-3"


@pytest.mark.asyncio
async def test_search_with_no_matches_returns_empty_results(
    search_app,
    fake_questions,
    passed_problem_ids,
):
    async with search_app.run_test() as pilot:
        search_input = search_app.screen.query_one("#search", Input)

        search_input.value = "does not exist"
        await pilot.pause()

        results = search_app.screen.query_one("#results", ListView)

        assert len(results.children) == 0


@pytest.mark.asyncio
async def test_empty_search_restores_all_problems(
    search_app,
    fake_questions,
    passed_problem_ids,
):
    async with search_app.run_test() as pilot:
        search_input = search_app.screen.query_one("#search", Input)

        search_input.value = "binary"
        await pilot.pause()

        results = search_app.screen.query_one("#results", ListView)
        assert len(results.children) == 1

        search_input.value = ""
        await pilot.pause()

        assert len(results.children) == 4


@pytest.mark.asyncio
async def test_search_filters_without_changing_original_problem_list(
    search_app,
    fake_questions,
    passed_problem_ids,
):
    async with search_app.run_test() as pilot:
        screen = search_app.screen
        search_input = screen.query_one("#search", Input)

        original = screen.problems.copy()

        search_input.value = "binary"
        await pilot.pause()

        assert screen.problems == original


@pytest.mark.asyncio
async def test_selecting_result_dismisses_with_problem_id(
    search_app,
    fake_questions,
    passed_problem_ids,
):
    async with search_app.run_test() as pilot:
        results = search_app.screen.query_one("#results", ListView)

        results.index = 2
        results.focus()

        await pilot.press("enter")
        await pilot.pause()

        assert search_app.result == 3
        assert not isinstance(search_app.screen, SearchScreen)


@pytest.mark.asyncio
async def test_selecting_first_result_returns_first_problem_id(
    search_app,
    fake_questions,
    passed_problem_ids,
):
    async with search_app.run_test() as pilot:
        results = search_app.screen.query_one("#results", ListView)

        results.index = 0
        results.focus()

        await pilot.press("enter")
        await pilot.pause()

        assert search_app.result == 1


@pytest.mark.asyncio
async def test_escape_dismisses_search_without_result(
    search_app,
    fake_questions,
    passed_problem_ids,
):
    async with search_app.run_test() as pilot:
        assert isinstance(search_app.screen, SearchScreen)

        await pilot.press("escape")
        await pilot.pause()

        assert search_app.result is None
        assert not isinstance(search_app.screen, SearchScreen)
