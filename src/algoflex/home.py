from textual.app import App
from textual.screen import Screen
from textual.containers import (
    Horizontal,
    Vertical,
    VerticalScroll,
    ItemGrid,
    VerticalGroup,
)
from textual.widgets import Footer, Label, Markdown, Button

PROBLEM_MD = """
```python
# Given an array of scores e.g [ '5', '2', 'C', 'D', '+', '+', 'C' ],
#  calculate the total points where:
#    +  add the last two scores.
#    D  double the last score.
#    C  cancel the last score and remove it.
#    x  add the score
# you're always guaranteed to have the last two scores for + and
# the previous score for D.
"""


class ProblemScreen(VerticalScroll):
    def compose(self):
        with VerticalScroll():
            yield Markdown(PROBLEM_MD)


class HomeScreen(App):
    def compose(self):
        yield Label("Algo Flex - The terminal code practice app")
        yield ProblemScreen()
        with HorizontalGroup():
            yield Button("attempt")
            yield Button("skip")
        yield Footer()


if __name__ == "__main__":
    app = HomeScreen()
    app.run()
