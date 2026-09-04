import time
from datetime import UTC, datetime

YEAR = 31_104_000
MONTH = 2_592_000
WEEK = 604_800
DAY = 86_400
HOUR = 3_600
MINUTE = 60
SECOND = 1


def time_ago(tm: float | str) -> str:
    if isinstance(tm, str):
        return tm

    elapsed = int(time.time() - tm)

    units = (
        (YEAR, "yr"),
        (MONTH, "mon"),
        (WEEK, "wk"),
        (DAY, "day"),
        (HOUR, "hr"),
        (MINUTE, "min"),
        (SECOND, "sec"),
    )

    for size, name in units:
        if elapsed >= size:
            value = elapsed // size
            return f"{value} {name}{'s' if value != 1 else ''} ago"

    return "Moments ago"


def fmt_secs(tm: float | str) -> str:
    if isinstance(tm, str):
        return tm

    def unit(value: int, singular: str) -> str:
        return f"{value} {singular if value == 1 else singular + 's'}"

    secs = int(tm)

    years, secs = divmod(secs, YEAR)
    months, secs = divmod(secs, MONTH)
    weeks, secs = divmod(secs, WEEK)
    days, secs = divmod(secs, DAY)
    hrs, secs = divmod(secs, HOUR)
    mins, secs = divmod(secs, MINUTE)

    if years:
        return f"{unit(years, 'yr')}, {unit(months, 'month')}"
    if months:
        return f"{unit(months, 'month')}, {unit(weeks, 'wk')}"
    if weeks:
        return f"{unit(weeks, 'wk')}, {unit(days, 'day')}"
    if days:
        return f"{unit(days, 'day')}, {unit(hrs, 'hr')}"
    if hrs:
        return f"{unit(hrs, 'hr')}, {unit(mins, 'min')}"
    if mins:
        return f"{unit(mins, 'min')}, {unit(secs, 'sec')}"
    return unit(secs, "second")


def midnight() -> float:
    """Return today's local midnight as a UTC Unix timestamp."""
    local_tz = datetime.now().astimezone().tzinfo
    now = datetime.now(local_tz)
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)

    return midnight.astimezone(UTC).timestamp()
