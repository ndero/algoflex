from textual.app import App
from textual.binding import Binding
from home import HomeScreen
from attempt import AttemptScreen


class AlgoFlex(App):
    MODES = {"home": HomeScreen, "attempt": AttemptScreen}
    DEFAULT_MODE = "home"
    BINDINGS = [
        Binding("h", "app.switch_mode('home')", "home", tooltip="Go to home"),
        Binding(
            "a",
            "app.switch_mode('attempt')",
            "attempt",
            tooltip="Attempt this question",
        ),
    ]

    def check_action(self, action, parameters):
        # disable footer switcher for current screen
        if (
            action == "switch_mode"
            and parameters
            and self.current_mode == parameters[0]
        ):
            return
        return True
