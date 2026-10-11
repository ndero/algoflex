from datetime import UTC, datetime

import pytest

from algoflex import utils


# Fixtures
@pytest.fixture
def freeze_time(monkeypatch):
    """Freeze `utils.time.time()` to a fixed Unix timestamp.

    Returns a callable that takes the timestamp to freeze at.
    """

    def _freeze(now: float) -> None:
        monkeypatch.setattr(utils.time, "time", lambda: now)

    return _freeze


@pytest.fixture
def freeze_datetime(monkeypatch):
    """Freeze `utils.datetime.now()` to a fixed datetime.

    Returns a callable that takes the datetime to freeze at. The frozen
    class passes the same instant to `now(tz=...)`, converting with
    `astimezone` so callers that request a specific zone still work.
    """

    def _freeze(now: datetime) -> None:
        class FrozenDateTime(datetime):
            @classmethod
            def now(cls, tz=None):
                if tz is None:
                    return now
                return now.astimezone(tz)

        monkeypatch.setattr(utils, "datetime", FrozenDateTime)

    return _freeze


# time_ago
class TestTimeAgo:
    @pytest.mark.parametrize(
        ("elapsed", "expected"),
        [
            (0, "Moments ago"),
            (1, "1 sec ago"),
            (30, "30 secs ago"),
            (59, "59 secs ago"),
            (60, "1 min ago"),
            (61, "1 min ago"),
            (119, "1 min ago"),
            (120, "2 mins ago"),
            (3_599, "59 mins ago"),
            (3_600, "1 hr ago"),
            (3_601, "1 hr ago"),
            (7_199, "1 hr ago"),
            (7_200, "2 hrs ago"),
            (86_399, "23 hrs ago"),
            (86_400, "1 day ago"),
            (172_800, "2 days ago"),
            (604_799, "6 days ago"),
            (604_800, "1 wk ago"),
            (1_209_600, "2 wks ago"),
            (2_592_000 - 1, "4 wks ago"),
            (2_592_000, "1 mon ago"),
            (5_184_000, "2 mons ago"),
            (31_104_000 - 1, "11 mons ago"),
            (31_104_000, "1 yr ago"),
            (62_208_000, "2 yrs ago"),
        ],
    )
    def test_relative_format(self, freeze_time, elapsed, expected):
        now = 1_000_000.0
        freeze_time(now)

        assert utils.time_ago(now - elapsed) == expected

    @pytest.mark.parametrize(
        "value",
        [
            "Just now",
            "1 min ago",
            "yesterday",
            "",
        ],
    )
    def test_preserves_strings(self, value):
        # Anything that isn't a numeric timestamp is returned unchanged.
        assert utils.time_ago(value) == value

    def test_truncates_fractional_elapsed_seconds(self, freeze_time):
        now = 1_000_000.0
        freeze_time(now)

        assert utils.time_ago(now - 59.9) == "59 secs ago"
        assert utils.time_ago(now - 60.9) == "1 min ago"

    def test_future_timestamp_is_moments_ago(self, freeze_time):
        freeze_time(1_000_000.0)

        assert utils.time_ago(1_000_001.0) == "Moments ago"


# fmt_secs
class TestFmtSecs:
    @pytest.mark.parametrize(
        ("seconds", "expected"),
        [
            (0, "0 seconds"),
            (1, "1 second"),
            (2, "2 seconds"),
            (59, "59 seconds"),
            (60, "1 min, 0 secs"),
            (61, "1 min, 1 sec"),
            (119, "1 min, 59 secs"),
            (120, "2 mins, 0 secs"),
            (3_599, "59 mins, 59 secs"),
            (3_600, "1 hr, 0 mins"),
            (3_601, "1 hr, 0 mins"),
            (3_660, "1 hr, 1 min"),
            (7_199, "1 hr, 59 mins"),
            (7_200, "2 hrs, 0 mins"),
            (86_399, "23 hrs, 59 mins"),
            (86_400, "1 day, 0 hrs"),
            (86_401, "1 day, 0 hrs"),
            (172_800, "2 days, 0 hrs"),
            (604_799, "6 days, 23 hrs"),
            (604_800, "1 wk, 0 days"),
            (604_801, "1 wk, 0 days"),
            (1_209_600, "2 wks, 0 days"),
            (2_592_000 - 1, "4 wks, 1 day"),
            (2_592_000, "1 month, 0 wks"),
            (5_184_000, "2 months, 0 wks"),
            (31_104_000 - 1, "11 months, 4 wks"),
            (31_104_000, "1 yr, 0 months"),
            (62_208_000, "2 yrs, 0 months"),
        ],
    )
    def test_format(self, seconds, expected):
        assert utils.fmt_secs(seconds) == expected

    @pytest.mark.parametrize(
        ("seconds", "expected"),
        [
            (1.9, "1 second"),
            (59.9, "59 seconds"),
            (60.9, "1 min, 0 secs"),
            (3_600.9, "1 hr, 0 mins"),
        ],
    )
    def test_truncates_fractional_seconds(self, seconds, expected):
        assert utils.fmt_secs(seconds) == expected

    @pytest.mark.parametrize(
        "value",
        [
            "0 seconds",
            "1 min, 30 secs",
            "1 hr, 5 mins",
            "Just now",
            "",
        ],
    )
    def test_preserves_strings(self, value):
        assert utils.fmt_secs(value) == value

    @pytest.mark.parametrize(
        ("seconds", "expected"),
        [
            (utils.MONTH - 1, "4 wks, 1 day"),
            (utils.MONTH, "1 month, 0 wks"),
            (utils.MONTH + utils.WEEK, "1 month, 1 wk"),
            (utils.YEAR - 1, "11 months, 4 wks"),
            (utils.YEAR, "1 yr, 0 months"),
            (utils.YEAR + utils.MONTH, "1 yr, 1 month"),
        ],
    )
    def test_uses_same_month_and_year_boundaries_as_time_ago(self, seconds, expected):
        # Guards the contract between time_ago and fmt_secs: both must
        # switch units at the same MONTH / YEAR constants, otherwise a
        # value near the boundary would be labelled with different top
        # units depending on which formatter ran.
        assert utils.fmt_secs(seconds) == expected


# midnight
class TestMidnight:
    def test_returns_today_local_midnight_as_utc(self, freeze_datetime):
        local_tz = datetime.now().astimezone().tzinfo
        frozen_now = datetime(2026, 9, 4, 14, 37, 52, tzinfo=local_tz)
        freeze_datetime(frozen_now)

        expected = datetime(2026, 9, 4, tzinfo=local_tz).astimezone(UTC).timestamp()

        assert utils.midnight() == expected
