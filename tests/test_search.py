import pytest
from textual.app import App
from textual.widgets import Input

from algoflex.search import SearchScreen


class TestApp(App):
    def on_mount(self) -> None:
        self.push_screen(SearchScreen())


@pytest.mark.asyncio
async def test_search_screen():
    async with TestApp().run_test() as pilot:
        screen = pilot.app.screen

        search = screen.query_one(Input)

        assert search.placeholder == "Search problems..."
