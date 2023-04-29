from textual.app import App
from textual.binding import Binding
from home import HomeScreen
from attempt import AttemptScreen


class AlgoFlex(App):
    MODES = {"home": HomeScreen, "attempt": AttemptScreen}
    DEFAULT_MODE = "home"
    BINDINGS = [
        Binding("h", "app.switch_mode('home')", "home", tooltip="show home screen"),
        Binding(
            "a", "app.switch_mode('attempt')", "attempt", tooltip="show attempt screen"
        ),
    ]
