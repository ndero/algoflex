import pytest

from algoflex.runner import ExecutionResult, run_solution
from algoflex.types import Language, RunStatus


@pytest.mark.asyncio
async def test_python_solution_passes():
    result = await run_solution(
        "x = 2 + 3",
        "assert x == 5",
        Language.PYTHON,
    )

    assert result == ExecutionResult(status=RunStatus.PASSED)


@pytest.mark.asyncio
async def test_python_solution_fails():
    result = await run_solution(
        "x = 2 + 3",
        "assert x == 6",
        Language.PYTHON,
    )

    assert result.status is RunStatus.FAILED
    assert result.stdout == ""
    assert "AssertionError" in result.stderr


@pytest.mark.asyncio
async def test_python_solution_captures_stdout():
    result = await run_solution(
        "print('hello')",
        "",
        Language.PYTHON,
    )

    assert result.status is RunStatus.PASSED
    assert result.stdout == "hello"
    assert result.stderr == ""


@pytest.mark.asyncio
async def test_python_solution_captures_stderr():
    result = await run_solution(
        "import sys; print('warning', file=sys.stderr)",
        "",
        Language.PYTHON,
    )

    assert result.status is RunStatus.PASSED
    assert result.stdout == ""
    assert result.stderr == "warning"


@pytest.mark.asyncio
async def test_python_solution_captures_stdout_and_stderr():
    result = await run_solution(
        """
import sys

print("stdout")
print("stderr", file=sys.stderr)
""",
        "",
        Language.PYTHON,
    )

    assert result.status is RunStatus.PASSED
    assert result.stdout == "stdout"
    assert result.stderr == "stderr"


@pytest.mark.asyncio
async def test_python_solution_streams_stdout_lines():
    lines: list[tuple[str, bool]] = []

    async def on_line(line: str, is_stderr: bool) -> None:
        lines.append((line, is_stderr))

    result = await run_solution(
        """
print("first")
print("second")
""",
        "",
        Language.PYTHON,
        on_line=on_line,
    )

    assert result.status is RunStatus.PASSED
    assert lines == [
        ("first", False),
        ("second", False),
    ]


@pytest.mark.asyncio
async def test_python_solution_streams_stderr_lines():
    lines: list[tuple[str, bool]] = []

    async def on_line(line: str, is_stderr: bool) -> None:
        lines.append((line, is_stderr))

    result = await run_solution(
        """
import sys

print("first", file=sys.stderr)
print("second", file=sys.stderr)
""",
        "",
        Language.PYTHON,
        on_line=on_line,
    )

    assert result.status is RunStatus.PASSED
    assert lines == [
        ("first", True),
        ("second", True),
    ]


@pytest.mark.asyncio
async def test_on_line_can_be_a_synchronous_callback():
    lines: list[tuple[str, bool]] = []

    def on_line(line: str, is_stderr: bool) -> None:
        lines.append((line, is_stderr))

    result = await run_solution(
        "print('hello')",
        "",
        Language.PYTHON,
        on_line=on_line,
    )

    assert result.status is RunStatus.PASSED
    assert lines == [("hello", False)]


@pytest.mark.asyncio
async def test_on_line_receives_stdout_and_stderr_in_stream_order():
    lines: list[tuple[str, bool]] = []

    def on_line(line: str, is_stderr: bool) -> None:
        lines.append((line, is_stderr))

    result = await run_solution(
        """
import sys

print("out-1", flush=True)
print("err-1", file=sys.stderr, flush=True)
print("out-2", flush=True)
print("err-2", file=sys.stderr, flush=True)
""",
        "",
        Language.PYTHON,
        on_line=on_line,
    )

    assert result.status is RunStatus.PASSED
    assert {line for line, _ in lines} == {
        "out-1",
        "out-2",
        "err-1",
        "err-2",
    }


@pytest.mark.asyncio
async def test_python_solution_times_out():
    result = await run_solution(
        """
import time

while True:
    time.sleep(1)
""",
        "",
        Language.PYTHON,
        timeout=0.05,
    )

    assert result.status is RunStatus.TIMEOUT
    assert result.stdout == ""
    assert result.stderr == ""


@pytest.mark.asyncio
async def test_python_runtime_error_is_failed():
    result = await run_solution(
        "raise ValueError('boom')",
        "",
        Language.PYTHON,
    )

    assert result.status is RunStatus.FAILED
    assert "ValueError" in result.stderr
    assert "boom" in result.stderr


@pytest.mark.asyncio
async def test_empty_python_user_code_can_run():
    result = await run_solution(
        "",
        "assert True",
        Language.PYTHON,
    )

    assert result.status is RunStatus.PASSED


@pytest.mark.asyncio
async def test_empty_python_test_code_can_run():
    result = await run_solution(
        "print('hello')",
        "",
        Language.PYTHON,
    )

    assert result.status is RunStatus.PASSED
    assert result.stdout == "hello"


@pytest.mark.asyncio
async def test_rust_solution_passes():
    result = await run_solution(
        """
fn main() {
    let value = 2 + 3;
    assert_eq!(value, 5);
    println!("hello");
}
""",
        "",
        Language.RUST,
    )

    assert result.status is RunStatus.PASSED
    assert result.stdout == "hello"
    assert result.stderr == ""


@pytest.mark.asyncio
async def test_rust_solution_fails_at_runtime():
    result = await run_solution(
        """
fn main() {
    panic!("boom");
}
""",
        "",
        Language.RUST,
    )

    assert result.status is RunStatus.FAILED
    assert "boom" in result.stderr


@pytest.mark.asyncio
async def test_rust_compile_error():
    result = await run_solution(
        """
fn main() {
    let x: i32 = "not an integer";
}
""",
        "",
        Language.RUST,
    )

    assert result.status is RunStatus.COMPILE_ERROR
    assert result.stdout == ""
    assert result.stderr


@pytest.mark.asyncio
async def test_rust_test_code_is_appended_to_user_code():
    result = await run_solution(
        """
fn add(a: i32, b: i32) -> i32 {
    a + b
}

fn main() {
""",
        """
    assert_eq!(add(2, 3), 5);
    println!("passed");
}
""",
        Language.RUST,
    )

    assert result.status is RunStatus.PASSED
    assert result.stdout == "passed"


@pytest.mark.asyncio
async def test_rust_solution_captures_stdout():
    result = await run_solution(
        """
fn main() {
    println!("hello");
    println!("world");
}
""",
        "",
        Language.RUST,
    )

    assert result.status is RunStatus.PASSED
    assert result.stdout == "hello\nworld"


@pytest.mark.asyncio
async def test_rust_solution_captures_stderr():
    result = await run_solution(
        """
fn main() {
    eprintln!("warning");
}
""",
        "",
        Language.RUST,
    )

    assert result.status is RunStatus.PASSED
    assert result.stderr == "warning"


@pytest.mark.asyncio
async def test_rust_solution_streams_output():
    lines: list[tuple[str, bool]] = []

    def on_line(line: str, is_stderr: bool) -> None:
        lines.append((line, is_stderr))

    result = await run_solution(
        """
fn main() {
    println!("hello");
    eprintln!("warning");
}
""",
        "",
        Language.RUST,
        on_line=on_line,
    )

    assert result.status is RunStatus.PASSED
    assert ("hello", False) in lines
    assert ("warning", True) in lines


@pytest.mark.asyncio
async def test_rust_solution_times_out():
    result = await run_solution(
        """
use std::thread;
use std::time::Duration;

fn main() {
    loop {
        thread::sleep(Duration::from_secs(1));
    }
}
""",
        "",
        Language.RUST,
        timeout=0.05,
    )

    assert result.status is RunStatus.TIMEOUT
    assert result.stdout == ""
    assert result.stderr == ""


@pytest.mark.asyncio
async def test_callback_strips_line_endings_but_not_content():
    lines: list[tuple[str, bool]] = []

    def on_line(line: str, is_stderr: bool) -> None:
        lines.append((line, is_stderr))

    result = await run_solution(
        "print('  hello  ')",
        "",
        Language.PYTHON,
        on_line=on_line,
    )

    assert result.status is RunStatus.PASSED
    assert lines == [("  hello", False)]
    assert result.stdout == "  hello"


@pytest.mark.asyncio
async def test_multiline_output_preserves_line_structure():
    result = await run_solution(
        """
print("one")
print("two")
print("three")
""",
        "",
        Language.PYTHON,
    )

    assert result.stdout == "one\ntwo\nthree"
