from textual.app import App
from textual.screen import Screen
from textual.containers import (
    Horizontal,
    Vertical,
    VerticalScroll,
    ItemGrid,
    VerticalGroup,
    HorizontalGroup,
    Center,
)
from textual.widgets import Footer, Label, Markdown, Button, Static
from textual.binding import Binding
from textual.reactive import Reactive
from _data import questions
from random import randint
from attempt import AttemptScreen
from custom_widgets import Title, Problem


class StatScreen(Vertical):
    DEFAULT_CSS = """
    Horizontal {
        Vertical {
            background: $boost;
            padding: 1;
            margin: 1 0;
        }
        #first {
            padding-bottom: 1;
        }
    }
    """

    def compose(self):
        with Horizontal():
            with Vertical():
                yield Static("[b]Attempts[/]", id="first")
                yield Static("2")
            with Vertical():
                yield Static("[b]Skips[/]", id="first")
                yield Static("5")
            with Vertical():
                yield Static("[b]Best time[/]", id="first")
                yield Static("...")
            with Vertical():
                yield Static("[b]Difficulty[/]", id="first")
                yield Static("[b green]Easy[/]")


class HomeScreen(App):
    BINDINGS = [
        Binding("a", "attempt", "attempt", tooltip="Attempt this question"),
        Binding("n", "next", "next", tooltip="Next question"),
    ]
    DEFAULT_CSS = """
    HomeScreen {
        Problem {
            height: 70vh;
            &>*{ max-width: 100; }
            align: center middle;
            margin-top: 1;
        }
        StatScreen {
            &>* {max-width: 100; }
            align: center middle;
        }
    }
    """
    problem_id = Reactive(-1)

    def compose(self):
        problem = questions.get(id, {}).get("markdown", "")
        yield Title()
        yield Problem(problem)
        yield StatScreen()
        yield Footer()

    def on_mount(self):
        self.problem_id = randint(0, 2)

    def watch_problem_id(self, id):
        problem = questions.get(id, {}).get("markdown", "")
        self.query_one(Problem).query_one(Markdown).update(markdown=problem)

    def action_attempt(self):
        self.push_screen(AttemptScreen(self.problem_id))

    def action_next(self):
        self.problem_id = randint(0, 2)

    def check_action(self, action, parameters):
        if not self.screen.id == "_default":
            if action == "attempt" or action == "next":
                return False
        return True
