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


class TitleScreen(Center):
    TITLE_MD = """
# Algo Flex - The terminal code practice app
"""

    def compose(self):
        yield Markdown(self.TITLE_MD)


class ProblemScreen(VerticalScroll):
    DEFAULT_CSS = """
    VerticalScroll {
        Markdown {
            height: 100%;
            padding: 0 1;
        }
    }
    """
    PROBLEM_MD = """
### Calculate the score
Given an array of scores e.g `[ '5', '2', 'C', 'D', '+', '+', 'C' ]`, calculate the total points where:
```
+  add the last two scores.
D  double the last score.
C  cancel the last score and remove it.
x  add the score
```
You're always guaranteed to have the last two scores for `+` and the previous score for `D`.
### Example
```
input: [ '5', '2', 'C', 'D', '+', '+', 'C' ]
output: 30
```
"""

    def compose(self):
        with VerticalScroll():
            yield Markdown(self.PROBLEM_MD)


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
                yield Static("/...")
            with Vertical():
                yield Static("[b]Difficulty[/]", id="first")
                yield Static("[b green]easy[/]")


class HomeScreen(Screen):
    BINDINGS = [Binding("s", "skip", "skip", tooltip="Skip this question")]
    DEFAULT_CSS = """
    HomeScreen {
        ProblemScreen {
            height: 66vh;
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

    def compose(self):
        yield TitleScreen()
        yield ProblemScreen()
        yield StatScreen()
        yield Footer()
