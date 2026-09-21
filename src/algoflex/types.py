import json
from dataclasses import dataclass
from enum import IntEnum
from functools import cached_property
from pathlib import Path
from typing import TypedDict


class Level(IntEnum):
    BREEZY = 1
    STEADY = 2
    EDGY = 3

    @property
    def label(self) -> str:
        return self.name.title()


class Language(IntEnum):
    PYTHON = 1
    RUST = 2

    @property
    def label(self) -> str:
        return self.name.title()

    @property
    def slug(self) -> str:
        return self.name.lower()

    @property
    def icon(self) -> str:
        icons = {self.PYTHON: "🐍", self.RUST: "🦀"}
        return icons[self]

    @property
    def suffix(self) -> str:
        suffixes = {self.PYTHON: ".py", self.RUST: ".rs"}
        return suffixes[self]


class RunStatus(IntEnum):
    PASSED = 1
    FAILED = 2
    TIMEOUT = 3
    ERROR = 4
    COMPILE_ERROR = 5

    @property
    def label(self) -> str:
        return self.name.title()

    @property
    def icon(self) -> str:
        return "🟢" if self is self.PASSED else "🔴"


class Attempt(TypedDict):
    problem_id: int
    status: RunStatus
    elapsed: float
    created_at: float
    code: str
    lang_id: Language


class Draft(TypedDict):
    problem_id: int
    lang_id: Language
    code: str
    elapsed: float
    updated_at: float


@dataclass(frozen=True)
class Question:
    id: int
    _metadata_path: Path
    _question_dir: Path
    _data_dir: Path

    @cached_property
    def _metadata(self) -> dict[str, str]:
        with self._metadata_path.open(encoding="utf-8") as file:
            return json.load(file)

    @cached_property
    def title(self) -> str:
        return self._metadata["title"]

    @cached_property
    def level(self) -> Level:
        return Level(self._metadata["level"])

    @cached_property
    def markdown(self) -> str:
        return self._read_file(self._question_dir / "problem.md")

    @cached_property
    def languages(self) -> list[Language]:
        """Return languages supported by this question."""
        return [
            language
            for language in Language
            if (self._question_dir / f"{language.slug}_starter.txt").is_file()
            and (
                self._question_dir / f"{language.slug}_tests{language.suffix}"
            ).is_file()
        ]

    @cached_property
    def python_starter(self) -> str:
        return self._read_file(self._question_dir / "python_starter.txt")

    @cached_property
    def python_tests(self) -> str:
        return self._read_file(self._data_dir / "run.py") + self._read_file(
            self._question_dir / "python_tests.py"
        )

    @cached_property
    def rust_starter(self) -> str:
        return self._read_file(self._question_dir / "rust_starter.txt")

    @cached_property
    def rust_tests(self) -> str:
        return self._read_file(self._data_dir / "run.rs") + self._read_file(
            self._question_dir / "rust_tests.rs"
        )

    @staticmethod
    def _read_file(path: Path) -> str:
        return path.read_text(encoding="utf-8")

    def starter_for(self, language: Language) -> str:
        return getattr(self, f"{language.slug}_starter")

    def tests_for(self, language: Language) -> str:
        return getattr(self, f"{language.slug}_tests")
