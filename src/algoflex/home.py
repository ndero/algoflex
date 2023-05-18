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


class HomeScreen(Screen):
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
        yield ProblemScreen()
        yield Footer()
