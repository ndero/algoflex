from dataclasses import dataclass
from enum import IntEnum
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


@dataclass(frozen=True, slots=True)
class Question:
    id: int
    title: str
    level: Level
    markdown: str
    python_tests: str
    rust_tests: str
    python_starter: str
    rust_starter: str

    def starter_for(self, language: Language) -> str:
        return getattr(self, f"{language.slug}_starter")

    def tests_for(self, language: Language) -> str:
        return getattr(self, f"{language.slug}_tests")
