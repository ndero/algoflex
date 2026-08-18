import json
from dataclasses import dataclass
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"


@dataclass(frozen=True, slots=True)
class Question:
    id: int
    title: str
    level: str
    markdown: str
    python_tests: str
    rust_tests: str
    python_starter: str
    rust_starter: str


class QuestionRepository:
    def __init__(self, data_dir: Path = DATA_DIR) -> None:
        self.data_dir = data_dir

    @property
    def ids(self) -> list[int]:
        """Return all available question IDs in ascending order."""
        return sorted(
            int(path.name)
            for path in self.data_dir.iterdir()
            if path.is_dir() and path.name.isdigit()
        )

    def get(self, question_id: int) -> Question:
        """Load and return a question by ID."""
        question_dir = self.data_dir / f"{question_id:02d}"

        if not question_dir.is_dir():
            raise KeyError(f"Question {question_id} does not exist")

        metadata = self._load_metadata(question_dir)
        python_runner = self._read_file(self.data_dir / "run.py")
        rust_runner = self._read_file(self.data_dir / "run.rs")

        return Question(
            id=question_id,
            title=metadata["title"],
            level=metadata["level"],
            markdown=self._read_file(question_dir / "problem.md"),
            python_starter=self._read_file(question_dir / "python_starter.txt"),
            python_tests=python_runner
            + self._read_file(question_dir / "python_tests.py"),
            rust_starter=self._read_file(question_dir / "rust_starter.txt"),
            rust_tests=rust_runner + self._read_file(question_dir / "rust_tests.rs"),
        )

    @staticmethod
    def _load_metadata(question_dir: Path) -> dict[str, str]:
        metadata_file = question_dir / "metadata.json"

        with metadata_file.open(encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def _read_file(path: Path) -> str:
        return path.read_text(encoding="utf-8")


questions = QuestionRepository()
