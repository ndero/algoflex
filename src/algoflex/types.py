from enum import IntEnum


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
        return icons.get(self, self.name)
