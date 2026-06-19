from textual.events import Mount
from textual.screen import ModalScreen
from textual.widgets import Input, ListView, ListItem, Label, Footer
from textual.containers import Vertical
from textual.reactive import reactive
from algoflex.questions import questions
from algoflex.db import attempts
from tinydb import Query

KV = Query()


class SearchScreen(ModalScreen):
    BINDINGS = [
        ("escape", "dismiss", "dismiss"),
    ]

    problems = reactive([])  # all problems
    target = reactive("")
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

    def compose(self):
        with Vertical(id="dialog"):
            yield Input(
                value=f"{self.target}",
                placeholder="Search problems...",
            )
            yield ListView(id="results")
        yield Footer()

    async def on_mount(self) -> None:
        passed = set(
            doc["problem_id"] for doc in attempts.search(KV.passed == True)
        )
        self.problems = [("✓" if pid in passed else " ", pid, q["title"]) for pid, q in questions.items()]
        await self.update_results(self.problems)

    async def on_input_changed(self, event: Input.Changed) -> None:
        self.target = event.value.strip().lower()
        results = [p for p in self.problems if (self.target in p[2].lower())]
        await self.update_results(results)

    async def update_results(self, results):
        list_view = self.query_one("#results", ListView)
        await list_view.clear()
        for passed, pid, title in results:
            list_view.append(
                ListItem(Label(f"{passed} [b]{title}[/]"), id=f"item-{pid}",)
            )

    def on_list_view_selected(self, event: ListView.Selected):
        selected = event.item.id or ""
        pid = int(selected.lstrip("item-"))
        self.dismiss(pid)
