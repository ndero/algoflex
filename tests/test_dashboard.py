from types import SimpleNamespace
from typing import ClassVar

import pytest
from textual.app import App, ComposeResult
from textual.widgets import Digits, Label, Markdown, ProgressBar, Static

from algoflex import dashboard
from algoflex.dashboard import Dashboard
from algoflex.types import Language, Level, RunStatus


# Test doubles and helper app
class FakeQuestions:
    ids: ClassVar = [1, 2, 3, 4, 5]

    def __init__(self):
        self._questions = {
            1: SimpleNamespace(title="Two Sum", level=Level.BREEZY),
            2: SimpleNamespace(title="Valid Parentheses", level=Level.BREEZY),
            3: SimpleNamespace(title="Binary Search", level=Level.STEADY),
            4: SimpleNamespace(title="Merge Intervals", level=Level.STEADY),
            5: SimpleNamespace(title="Trap Rain Water", level=Level.EDGY),
        }

    def get(self, problem_id):
        return self._questions[problem_id]


class DashboardApp(App):
    def compose(self) -> ComposeResult:
        yield Dashboard()


@pytest.fixture
def fake_questions(monkeypatch):
    questions = FakeQuestions()
    monkeypatch.setattr(dashboard, "q", questions)
    return questions


@pytest.fixture
def dashboard_app(fake_questions):
    return DashboardApp()


def make_attempt(
    problem_id: int,
    status: RunStatus = RunStatus.PASSED,
    elapsed: float = 60.0,
    created_at: float = 1_000.0,
    lang_id: Language = Language.PYTHON,
):
    return {
        "problem_id": problem_id,
        "status": status,
        "elapsed": elapsed,
        "created_at": created_at,
        "lang_id": lang_id,
    }


def stub_summary_sources(
    monkeypatch,
    *,
    recent=None,
    frequent=None,
    best=None,
    fmt_secs=None,
    time_ago=None,
):
    monkeypatch.setattr(dashboard, "get_recent_attempts", lambda n: recent or [])
    monkeypatch.setattr(
        dashboard, "get_most_attempted_problems", lambda n: frequent or []
    )
    monkeypatch.setattr(dashboard, "get_best_attempts", lambda n: best or [])

    if fmt_secs is not None:
        monkeypatch.setattr(dashboard, "fmt_secs", fmt_secs)
    if time_ago is not None:
        monkeypatch.setattr(dashboard, "time_ago", time_ago)


def make_screen_dashboard(monkeypatch) -> Dashboard:
    """Build a detached Dashboard with problem levels pre-populated."""
    widget = Dashboard()
    widget.breezy, widget.steady, widget.edgy = widget.problem_levels()
    return widget


# Composition
class TestComposition:
    @pytest.mark.asyncio
    async def test_composes_expected_widgets(self, dashboard_app):
        async with dashboard_app.run_test():
            assert dashboard_app.query_one("#title", Static)
            assert dashboard_app.query_one("#breezy_complete", Digits)
            assert dashboard_app.query_one("#breezy_total", Label)
            assert dashboard_app.query_one("#steady_complete", Digits)
            assert dashboard_app.query_one("#steady_total", Label)
            assert dashboard_app.query_one("#edgy_complete", Digits)
            assert dashboard_app.query_one("#edgy_total", Label)
            assert dashboard_app.query_one("#all", ProgressBar)
            assert dashboard_app.query_one("#today", Static)
            assert dashboard_app.query_one("#recent", Markdown)
            assert dashboard_app.query_one("#frequent", Markdown)
            assert dashboard_app.query_one("#best", Markdown)


# Problem classification
class TestProblemLevels:
    def test_classifies_questions(self, fake_questions):
        breezy, steady, edgy = Dashboard().problem_levels()

        assert breezy == {1, 2}
        assert steady == {3, 4}
        assert edgy == {5}

    def test_does_not_duplicate_problem_ids(self, fake_questions):
        fake_questions.ids = [1, 1, 2, 3]

        breezy, steady, edgy = Dashboard().problem_levels()

        assert breezy == {1, 2}
        assert steady == {3}
        assert edgy == set()


# Totals displayed in the header
class TestTotals:
    @pytest.mark.asyncio
    async def test_initializes_problem_totals(self, dashboard_app, fake_questions):
        async with dashboard_app.run_test():
            widget = dashboard_app.query_one(Dashboard)

            assert widget.breezy == {1, 2}
            assert widget.steady == {3, 4}
            assert widget.edgy == {5}

            assert widget.total == (
                len(widget.breezy) * Level.BREEZY
                + len(widget.steady) * Level.STEADY
                + len(widget.edgy) * Level.EDGY
            )

    @pytest.mark.asyncio
    async def test_displays_problem_totals(self, dashboard_app, fake_questions):
        async with dashboard_app.run_test():
            breezy = dashboard_app.query_one("#breezy_total", Label)
            steady = dashboard_app.query_one("#steady_total", Label)
            edgy = dashboard_app.query_one("#edgy_total", Label)

            assert str(breezy.render()) == "of 2"
            assert str(steady.render()) == "of 2"
            assert str(edgy.render()) == "of 1"

    @pytest.mark.asyncio
    async def test_progress_bar_starts_at_zero(self, dashboard_app, fake_questions):
        async with dashboard_app.run_test():
            progress = dashboard_app.query_one("#all", ProgressBar)

            assert progress.progress == 0
            assert progress.total == (
                2 * Level.BREEZY + 2 * Level.STEADY + 1 * Level.EDGY
            )


# Completion calculations
class TestGetComplete:
    def test_counts_passed_problems(self, fake_questions, monkeypatch):
        monkeypatch.setattr(dashboard, "get_passed_problem_ids", lambda: {1, 3, 5})

        widget = make_screen_dashboard(monkeypatch)

        assert widget.get_complete() == (1, 1, 1)

    def test_ignores_failed_problems(self, fake_questions, monkeypatch):
        monkeypatch.setattr(dashboard, "get_passed_problem_ids", lambda: set())

        widget = make_screen_dashboard(monkeypatch)

        assert widget.get_complete() == (0, 0, 0)

    def test_only_counts_passed_ids_that_exist(self, fake_questions, monkeypatch):
        monkeypatch.setattr(dashboard, "get_passed_problem_ids", lambda: {1, 999})

        widget = make_screen_dashboard(monkeypatch)

        assert widget.get_complete() == (1, 0, 0)


# Markdown table builder
class TestMdTable:
    def test_returns_no_records_message_for_empty_rows(self):
        assert Dashboard().md_table(["Problem", "Level"], []) == (
            "\n\nNo records yet\n\n"
        )

    def test_builds_markdown_table(self):
        result = Dashboard().md_table(
            ["Problem", "Level"],
            [
                ("Two Sum", "Breezy"),
                ("Binary Search", "Steady"),
            ],
        )

        assert result == (
            "|Problem|Level|\n|---|---|\n|Two Sum|Breezy|\n|Binary Search|Steady|"
        )

    def test_converts_values_to_strings(self):
        result = Dashboard().md_table(
            ["Problem", "Attempts"],
            [("Two Sum", 3)],
        )

        assert "|Two Sum|3|" in result


# Today's highlight comment
class TestHighlightComment:
    @pytest.mark.parametrize(
        ("passed", "attempts"),
        [(0, 0), (0, 5), (0, 6), (0, 20)],
    )
    def test_with_no_passes(self, passed, attempts):
        comment = Dashboard().get_highlight_comment(passed, attempts)

        if attempts < 6:
            assert comment == "Not bad"
        else:
            assert comment == "D for dust"

    @pytest.mark.parametrize("passed", [1, 2])
    def test_for_one_or_two_passes(self, passed, monkeypatch):
        monkeypatch.setattr(dashboard, "choice", lambda values: values[0])

        assert Dashboard().get_highlight_comment(passed, 5) == "Solid"

    @pytest.mark.parametrize("passed", [3, 4])
    def test_for_three_or_four_passes(self, passed, monkeypatch):
        monkeypatch.setattr(dashboard, "choice", lambda values: values[0])

        assert Dashboard().get_highlight_comment(passed, 5) == "Excellent"

    @pytest.mark.parametrize("passed", [5, 6, 7, 8])
    def test_for_five_to_eight_passes(self, passed, monkeypatch):
        monkeypatch.setattr(dashboard, "choice", lambda values: values[0])

        assert Dashboard().get_highlight_comment(passed, 10) == "Wizard"

    def test_for_nine_or_more_passes(self):
        widget = Dashboard()

        assert widget.get_highlight_comment(9, 10) == "Ace"
        assert widget.get_highlight_comment(20, 20) == "Ace"


# Today's highlight assembly
class TestTodayHighlight:
    def test_reads_attempts_today_and_comment(self, monkeypatch):
        widget = Dashboard()

        monkeypatch.setattr(dashboard, "get_attempts_today", lambda: (3, 7))
        monkeypatch.setattr(
            widget,
            "get_highlight_comment",
            lambda passed, attempts: "Excellent",
        )

        assert widget.get_today_highlight() == ("Excellent", 3, 7)


# Summary data
class TestSummaryData:
    def test_builds_recent_attempts(self, fake_questions, monkeypatch):
        stub_summary_sources(
            monkeypatch,
            recent=[
                make_attempt(1, RunStatus.PASSED, elapsed=65, created_at=1_000),
                make_attempt(
                    3,
                    RunStatus.FAILED,
                    elapsed=120,
                    created_at=2_000,
                    lang_id=Language.RUST,
                ),
            ],
            fmt_secs=lambda value: f"duration:{value}",
            time_ago=lambda value: f"when:{value}",
        )

        recent, frequent, best = Dashboard().get_summary()

        assert recent == [
            (
                "✓ Two Sum",
                Level.BREEZY.label,
                Language.PYTHON.label,
                "duration:65",
                "when:1000",
            ),
            (
                "x Binary Search",
                Level.STEADY.label,
                Language.RUST.label,
                "duration:120",
                "when:2000",
            ),
        ]
        assert frequent == []
        assert best == []

    def test_builds_frequent_attempts(self, fake_questions, monkeypatch):
        stub_summary_sources(
            monkeypatch,
            frequent=[
                {"problem_id": 1, "passed_count": 2, "total_count": 5},
                {"problem_id": 3, "passed_count": 1, "total_count": 2},
            ],
        )

        recent, frequent, best = Dashboard().get_summary()

        assert recent == []
        assert frequent == [
            ("Two Sum", Level.BREEZY.label, "2/5"),
            ("Binary Search", Level.STEADY.label, "1/2"),
        ]
        assert best == []

    def test_builds_personal_bests(self, fake_questions, monkeypatch):
        stub_summary_sources(
            monkeypatch,
            best=[
                make_attempt(
                    5,
                    RunStatus.PASSED,
                    elapsed=25,
                    created_at=3_000,
                    lang_id=Language.RUST,
                )
            ],
            fmt_secs=lambda value: f"duration:{value}",
            time_ago=lambda value: f"when:{value}",
        )

        recent, frequent, best = Dashboard().get_summary()

        assert recent == []
        assert frequent == []
        assert best == [
            (
                "✓ Trap Rain Water",
                Level.EDGY.label,
                Language.RUST.label,
                "duration:25",
                "when:3000",
            )
        ]


# Individual widget updaters
class TestUpdateDigits:
    @pytest.mark.asyncio
    async def test_updates_completion_counts(self, dashboard_app, fake_questions):
        async with dashboard_app.run_test():
            widget = dashboard_app.query_one(Dashboard)

            widget.update_digits(1, 2, 3)

            assert widget.breezy_complete.value == "1"
            assert widget.steady_complete.value == "2"
            assert widget.edgy_complete.value == "3"


class TestUpdateProgress:
    @pytest.mark.asyncio
    async def test_updates_progress_bar(self, dashboard_app, fake_questions):
        async with dashboard_app.run_test():
            widget = dashboard_app.query_one(Dashboard)

            widget.update_progress(5)

            assert widget.progress_bar.progress == 5


class TestUpdateHighlight:
    @pytest.mark.asyncio
    async def test_hides_highlight_when_no_attempts(
        self, dashboard_app, fake_questions, monkeypatch
    ):
        monkeypatch.setattr(dashboard, "get_attempts_today", lambda: (0, 0))

        async with dashboard_app.run_test():
            widget = dashboard_app.query_one(Dashboard)

            assert widget.today.display is False

            widget.update_highlight()

            assert widget.today.display is False

    @pytest.mark.asyncio
    async def test_displays_today_summary(
        self, dashboard_app, fake_questions, monkeypatch
    ):
        monkeypatch.setattr(dashboard, "get_attempts_today", lambda: (2, 4))
        monkeypatch.setattr(dashboard, "choice", lambda values: values[0])

        async with dashboard_app.run_test():
            widget = dashboard_app.query_one(Dashboard)

            widget.update_highlight()

            assert widget.today.display is True
            assert widget.today.border_title == "Today's highlight"

            rendered = str(widget.today.render())

            assert "Solid!" in rendered
            assert "Solved" in rendered
            assert "2" in rendered
            assert "4" in rendered


# Summary rendering
class TestUpdateSummary:
    @pytest.mark.asyncio
    async def test_updates_all_three_markdown_widgets(
        self, dashboard_app, fake_questions, monkeypatch
    ):
        stub_summary_sources(
            monkeypatch,
            recent=[make_attempt(1, RunStatus.PASSED)],
            frequent=[{"problem_id": 3, "passed_count": 2, "total_count": 4}],
            best=[make_attempt(5, RunStatus.PASSED, lang_id=Language.RUST)],
            fmt_secs=lambda value: "1 min",
            time_ago=lambda value: "Just now",
        )

        async with dashboard_app.run_test():
            widget = dashboard_app.query_one(Dashboard)

            received = {}

            monkeypatch.setattr(
                widget.recent_markdown,
                "update",
                lambda value: received.__setitem__("recent", value),
            )
            monkeypatch.setattr(
                widget.frequent_markdown,
                "update",
                lambda value: received.__setitem__("frequent", value),
            )
            monkeypatch.setattr(
                widget.best_markdown,
                "update",
                lambda value: received.__setitem__("best", value),
            )

            widget.update_summary()

            assert "Two Sum" in received["recent"]
            assert "Binary Search" in received["frequent"]
            assert "2/4" in received["frequent"]
            assert "Trap Rain Water" in received["best"]


# Reactive visibility
class TestReactiveVisibility:
    @pytest.mark.asyncio
    async def test_showing_dashboard_updates_dashboard(
        self, dashboard_app, fake_questions, monkeypatch
    ):
        monkeypatch.setattr(Dashboard, "get_complete", lambda self: (1, 1, 1))
        monkeypatch.setattr(
            Dashboard, "get_today_highlight", lambda self: ("Solid", 2, 3)
        )
        stub_summary_sources(monkeypatch)

        async with dashboard_app.run_test():
            widget = dashboard_app.query_one(Dashboard)

            widget.show_dashboard = True

            assert widget.breezy_complete.value == "1"
            assert widget.steady_complete.value == "1"
            assert widget.edgy_complete.value == "1"

            assert widget.progress_bar.progress == (
                Level.BREEZY + Level.STEADY + Level.EDGY
            )
