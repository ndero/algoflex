from functools import cached_property
from pathlib import Path

from algoflex.types import Question

DATA_DIR = Path(__file__).parent / "data"


class QuestionRepository:
    def __init__(self, data_dir: Path = DATA_DIR) -> None:
        self.data_dir = data_dir

    @cached_property
    def ids(self) -> set[int]:
        """Return a set of all available question IDs"""
        return {
            int(path.name)
            for path in self.data_dir.iterdir()
            if path.is_dir() and path.name.isdigit()
        }

    def get(self, question_id: int) -> Question:
        """Return a question by ID."""
        question_dir = self.data_dir / f"{question_id:02d}"

        if not question_dir.is_dir():
            raise KeyError(f"Question {question_id} does not exist")

        return Question(
            id=question_id,
            _metadata_path=question_dir / "metadata.json",
            _question_dir=question_dir,
            _data_dir=self.data_dir,
        )


questions = QuestionRepository()
