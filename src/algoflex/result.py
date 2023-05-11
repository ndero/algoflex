from textual.screen import ModalScreen
from textual.widgets import Log, Button, TextArea
from textual.containers import VerticalGroup, Center
import textwrap
import tempfile
import subprocess
import os
from textual.app import App


class ResultModal(ModalScreen):
    BINDINGS = [("q", "dismiss", "dismiss")]
    DEFAULT_CSS = """
    ResultModal {
        align: center middle;
        width: 50;
    }
    """
    TEST_CODE = textwrap.dedent(
        """
        def run_tests():
            test_cases = [
                (([2, 7, 11, 15], 9), [0, 1]),
                (([3, 2, 4], 6), [1, 2]),
                (([3, 3], 6), [0, 1]),
                (([1, 2, 3], 4), [0, 2]),
            ]
            passed = 0
            for i, (inputs, expected) in enumerate(test_cases):
                try:
                    result = solution(*inputs)
                    if result == expected:
                        print(f"Test case {i+1} passed ✅")
                        passed += 1
                    else:
                        print(f"Test case {i+1} failed ❌ — got {result}, expected {expected}")
                except Exception as e:
                    print(f"Test case {i+1} error ❌ — {e}")
            print(f"\\nPassed {passed}/{len(test_cases)} test cases.")

        if __name__ == "__main__":
            run_tests()
        """
    )

    def __init__(self, code):
        super().__init__()
        self.code = code

    def on_mount(self):
        self.run_user_code()

    def compose(self):
        with VerticalGroup(id="code"):
            yield Log(highlight=True)
            yield TextArea("Passed!")
            yield Button("Ok")

    def run_user_code(self):
        user_code = self.code.strip()
        output_log = self.query_one(Log)
        full_code = f"{user_code}\n\n{self.TEST_CODE}"
        with tempfile.NamedTemporaryFile(
            delete=False, suffix=".py", mode="w"
        ) as tmp_file:
            tmp_file.write(full_code)
        try:
            result = subprocess.run(
                ["python3", tmp_file.name], capture_output=True, text=True, timeout=10
            )
            if result.stdout:
                output_log.write(result.stdout)
            if result.stderr:
                output_log.write(f"[red]{result.stderr}[/red]")
        except subprocess.TimeoutExpired:
            output_log.write("Execution timed out")
        except Exception as e:
            output_log.write("Error running code")
        finally:
            os.remove(tmp_file.name)
