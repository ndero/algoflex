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
from random import shuffle
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
        Binding("p", "previous", "previous", tooltip="Previous question"),
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
    problem_id = Reactive(0)
    index = 0
    PROBLEMS_COUNT = len(questions.keys())
    PROBLEMS = [i for i in range(PROBLEMS_COUNT)]

    def compose(self):
        problem = questions.get(id, {}).get("markdown", "")
        yield Title()
        yield Problem(problem)
        yield StatScreen()
        yield Footer()

    def on_mount(self):
        shuffle(self.PROBLEMS)
        self.problem_id = self.PROBLEMS[self.index]

    def watch_problem_id(self, id):
        problem = questions.get(id, {}).get("markdown", "")
        self.query_one(Problem).query_one(Markdown).update(markdown=problem)

    def action_attempt(self):
        self.push_screen(AttemptScreen(self.problem_id))

    def action_next(self):
        if self.index + 1 < self.PROBLEMS_COUNT:
            self.index += 1
        self.problem_id = self.PROBLEMS[self.index]

    def action_previous(self):
        if self.index > 0:
            self.index -= 1
        self.problem_id = self.PROBLEMS[self.index]

    def check_action(self, action, parameters):
        if not self.screen.id == "_default":
            if action == "attempt" or action == "next":
                return False
        return True
