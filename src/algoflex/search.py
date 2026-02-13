from textual.events import Mount
from textual.screen import ModalScreen
from textual.widgets import Input, ListView, ListItem, Label, Footer
from textual.containers import Vertical
from textual.reactive import reactive
from algoflex.questions import questions
from algoflex.db import get_db
from tinydb import Query

KV = Query()
attempts = get_db()


class SearchScreen(ModalScreen):
    BINDINGS = [
        ("escape", "dismiss", "dismiss"),
    ]

    matches = reactive([], recompose=True)
    target = reactive("")
    passed = reactive(set)
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
                id="search",
                select_on_focus=False,
            )
            with ListView():
                for passed, pid, title in self.matches:
                    yield ListItem(
                        Label(f"{passed} [b]{title}[/]"),
                        id=f"item-{pid}",
                    )
        yield Footer()

    def on_mount(self) -> None:
        self.passed = set(
            doc["problem_id"] for doc in attempts.search(KV.passed == True)
        )

    def on_input_changed(self, event: Input.Changed) -> None:
        self.target = event.value.strip().lower() or ""
        self.update_results()
        self.query_one("#search", Input).focus()

    def update_results(self):
        matches = (
            []
            if len(self.target) < 2
            else [
                ("✓" if pid in self.passed else " ", pid, q["title"])
                for pid, q in questions.items()
                if (self.target in q["title"].lower())
            ]
        )
        self.matches = matches

    def on_list_view_selected(self, event: ListView.Selected):
        selected = event.item.id or ""
        pid = int(selected.lstrip("item-"))
        self.dismiss(pid)
