from __future__ import annotations

import asyncio
import sys
import tempfile
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from pathlib import Path

from algoflex.types import Language, RunStatus

TIMEOUT = 9.0

LineCallback = Callable[[str, bool], Awaitable[None] | None]


@dataclass(slots=True)
class ExecutionResult:
    status: RunStatus
    stdout: str = ""
    stderr: str = ""


async def run_solution(
    user_code: str,
    test_code: str,
    language: Language,
    *,
    on_line: LineCallback | None = None,
    timeout: float = TIMEOUT,
) -> ExecutionResult:
    source = f"{user_code.strip()}\n\n{test_code}"

    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        source_path = tmp_dir / f"main{language.suffix}"

        source_path.write_text(source, encoding="utf-8")

        executable_path = tmp_dir / "main"
        if language is Language.RUST:
            return await _run_rust(
                source_path,
                executable_path,
                on_line=on_line,
                timeout=timeout,
            )

        return await _run_python(
            source_path,
            on_line=on_line,
            timeout=timeout,
        )


async def _run_python(
    source_path: Path,
    *,
    on_line: LineCallback | None,
    timeout: float,
) -> ExecutionResult:
    proc = await asyncio.create_subprocess_exec(
        sys.executable,
        "-u",
        str(source_path),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    return await _collect_process(
        proc,
        on_line=on_line,
        timeout=timeout,
    )


async def _run_rust(
    source_path: Path,
    executable_path: Path,
    *,
    on_line: LineCallback | None,
    timeout: float,
) -> ExecutionResult:
    compile_proc = await asyncio.create_subprocess_exec(
        "rustc",
        "--edition",
        "2024",
        "-O",
        str(source_path),
        "-o",
        str(executable_path),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    stdout, stderr = await compile_proc.communicate()

    if compile_proc.returncode != 0:
        return ExecutionResult(
            status=RunStatus.COMPILE_ERROR,
            stdout=stdout.decode(errors="replace"),
            stderr=stderr.decode(errors="replace"),
        )

    proc = await asyncio.create_subprocess_exec(
        str(executable_path),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    return await _collect_process(
        proc,
        on_line=on_line,
        timeout=timeout,
    )


async def _collect_process(
    proc: asyncio.subprocess.Process,
    *,
    on_line: LineCallback | None,
    timeout: float,
) -> ExecutionResult:
    async def read_stream(
        stream: asyncio.StreamReader | None,
        is_stderr: bool,
    ) -> str:
        if stream is None:
            return ""

        lines: list[str] = []

        async for raw_line in stream:
            line = raw_line.decode(errors="replace").rstrip()
            lines.append(line)

            if on_line:
                result = on_line(line, is_stderr)
                if asyncio.iscoroutine(result):
                    await result

        return "\n".join(lines)

    stdout_task = asyncio.create_task(read_stream(proc.stdout, False))
    stderr_task = asyncio.create_task(read_stream(proc.stderr, True))

    try:
        await asyncio.wait_for(
            proc.wait(),
            timeout=timeout,
        )
    except TimeoutError:
        proc.kill()
        await proc.wait()
        stdout_task.cancel()
        stderr_task.cancel()
        await asyncio.gather(
            stdout_task,
            stderr_task,
            return_exceptions=True,
        )

        return ExecutionResult(status=RunStatus.TIMEOUT)
    else:
        stdout, stderr = await asyncio.gather(
            stdout_task,
            stderr_task,
        )

    status = RunStatus.PASSED if proc.returncode == 0 else RunStatus.FAILED

    return ExecutionResult(
        status=status,
        stdout=stdout,
        stderr=stderr,
    )
