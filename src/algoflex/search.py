from typing import ClassVar

from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import ModalScreen
from textual.widgets import Footer, Input, Label, ListItem, ListView

from algoflex.db import get_passed_problem_ids
from algoflex.questions import questions


class SearchScreen(ModalScreen):
    BINDINGS: ClassVar = [
        ("escape", "dismiss", "dismiss"),
    ]

    DEFAULT_CSS = """
    SearchScreen {
        align: center middle;
    }

    #dialog {
        height: 80vh;
        width: 60vw;
        background: $boost;
        padding: 1 2;
    }

    #search {
        margin-bottom: 1;
    }

    ListItem {
        padding: 1;
        margin: 0 1;
    }
    """

    def __init__(self) -> None:
        super().__init__()
        self.problems: list[tuple[str, int, str]] = []

    def compose(self) -> ComposeResult:
        with Vertical(id="dialog"):
            yield Input(
                id="search",
                placeholder="Search problems...",
            )
            yield ListView(id="results")
        yield Footer()

    async def on_mount(self) -> None:
        self.list_view = self.query_one("#results", ListView)

        passed = get_passed_problem_ids()
        self.problems = [
            (
                "✓" if pid in passed else " ",
                pid,
                questions.get(pid).title,
            )
            for pid in questions.ids
        ]
        await self.update_results(self.problems)

    async def on_input_changed(self, event: Input.Changed) -> None:
        target = event.value.strip().casefold()
        results = [p for p in self.problems if (target in p[2].casefold())]
        await self.update_results(results)

    async def update_results(self, results) -> None:
        await self.list_view.clear()
        for passed, pid, title in results:
            self.list_view.append(
                ListItem(
                    Label(f"{passed} [b]{title}[/]"),
                    id=f"item-{pid}",
                )
            )

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        selected = event.item.id or ""
        pid = int(selected.removeprefix("item-"))
        self.dismiss(pid)
