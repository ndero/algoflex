from datetime import UTC, datetime

import pytest

from algoflex import utils


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
        (31_103_999, "11 mons ago"),
        (31_104_000, "1 yr ago"),
        (62_208_000, "2 yrs ago"),
    ],
)
def test_time_ago(monkeypatch, elapsed, expected):
    now = 1_000_000.0
    monkeypatch.setattr(utils.time, "time", lambda: now)

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
def test_time_ago_preserves_strings(value):
    assert utils.time_ago(value) == value


def test_time_ago_truncates_fractional_elapsed_seconds(monkeypatch):
    now = 1_000_000.0
    monkeypatch.setattr(utils.time, "time", lambda: now)

    assert utils.time_ago(now - 59.9) == "59 secs ago"
    assert utils.time_ago(now - 60.9) == "1 min ago"


def test_time_ago_future_timestamp_is_just_now(monkeypatch):
    monkeypatch.setattr(utils.time, "time", lambda: 1_000_000.0)

    assert utils.time_ago(1_000_001.0) == "Moments ago"


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
def test_fmt_secs(seconds, expected):
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
def test_fmt_secs_truncates_fractional_seconds(seconds, expected):
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
def test_fmt_secs_preserves_strings(value):
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
def test_fmt_secs_uses_same_month_and_year_boundaries_as_time_ago(
    seconds,
    expected,
):
    assert utils.fmt_secs(seconds) == expected


def test_midnight_returns_today_local_midnight_as_utc(monkeypatch):
    local_tz = datetime.now().astimezone().tzinfo
    frozen_now = datetime(
        2026,
        9,
        4,
        14,
        37,
        52,
        tzinfo=local_tz,
    )

    class FrozenDateTime(datetime):
        @classmethod
        def now(cls, tz=None):
            if tz is None:
                return frozen_now

            return frozen_now.astimezone(tz)

    monkeypatch.setattr(utils, "datetime", FrozenDateTime)

    expected = (
        datetime(
            2026,
            9,
            4,
            tzinfo=local_tz,
        )
        .astimezone(UTC)
        .timestamp()
    )

    assert utils.midnight() == expected
