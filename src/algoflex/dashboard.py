from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal, Center, Grid, HorizontalGroup
from textual.reactive import reactive
from textual.widgets import (
    ProgressBar,
    Digits,
    Static,
    Label,
    Collapsible,
    DataTable,
    Markdown,
)
from textual.widget import Widget
from algoflex.questions import questions as q
from algoflex.db import get_db
from algoflex.utils import time_ago, fmt_secs
from tinydb import Query
from heapq import nlargest, nsmallest
from collections import Counter

KV = Query()
attempts = get_db()


class Dashboard(Widget):
    show_dashboard = reactive(False)
    # get completed questions per level
    docs, breezy, steady, edgy = attempts.all(), set(), set(), set()
    for k, v in q.items():
        if v["level"] == "Breezy":
            breezy.add(k)
        elif v["level"] == "Steady":
            steady.add(k)
        else:
            edgy.add(k)
    total = len(q)

    DEFAULT_CSS = """
    Dashboard {
        overflow-y: auto;
        width: 50vw;
        border-left: vkey $boost;
        border-right: vkey $boost;
        padding: 1 2;
        layer: dashboard; 
        align-horizontal: center;
        dock: top;
        offset-x: 100vw;
        transition: offset 200ms;  
        &.-visible {
            offset-x: 50vw;
        }

        Bar {
            & > .bar--bar {
                color: $markdown-h1-color;
            }
        }

        #breezy {
            color: green 90%;
        }

        #steady {
            color: orange 70%;
        }

        #edgy {
            color: red 70%;
        }


        #title {
            height: 4;
            color: $markdown-h1-color;
            content-align: center middle;
        }

        #counts {
            height: 7;
        }

        Digits {
            text-align: center;
        }

        #progress {
            height: 3;
        }
    }
    """

    def compose(self) -> ComposeResult:
        with Center(id="dashboard"):
            yield Static("Dashboard", id="title")
            with Horizontal(id="counts"):
                with Center(id="breezy"):
                    yield Center(Label("Breezy"))
                    yield Digits("0", id="d_breezy")
                    yield Center(Label(f"of {len(self.breezy)}"))
                with Center(id="steady"):
                    yield Center(Label("Steady"))
                    yield Digits("0", id="d_steady")
                    yield Center(Label(f"of {len(self.steady)}"))
                with Center(id="edgy"):
                    yield Center(Label("Edgy"))
                    yield Digits("0", id="d_edgy")
                    yield Center(Label(f"of {len(self.edgy)}"))
            with Center(id="progress"):
                yield ProgressBar(total=self.total, show_eta=False, id="all")
            with Collapsible(title="Recent"):
                yield Markdown(id="recent")
            with Collapsible(title="Frequent"):
                yield Markdown(id="frequent")
            with Collapsible(title="Best"):
                yield Markdown(id="best")
            with Collapsible(title="Worst"):
                yield Markdown(id="worst")

    def watch_show_dashboard(self) -> None:
        ids = ["#d_breezy", "#d_steady", "#d_edgy"]
        if self.show_dashboard:
            docs = attempts.all()
            breezy, steady, edgy = self.get_complete(docs)
            self.update_digits(ids, [breezy, steady, edgy])
            self.update_progress(breezy + steady + edgy)
            self.update_md(docs)
        else:
            self.update_digits(ids, [0, 0, 0])

    def animate_digit(self, id, value):
        target = self.query_one(f"{id}", Digits)
        if value < 1:
            target.update(f"{value}")
            return
        start = 0

        def update_digit():
            nonlocal start
            target.update(f"{start}")
            start += 1

        self.set_interval(
            value / (value * 15),
            update_digit,
            repeat=value,
        )

    def md_table(self, headers, rows):
        if not rows:
            return "\n\nNo records yet\n\n"
        sep = "|" + "|".join(["---"] * len(headers)) + "|"
        head = "|" + "|".join(headers) + "|"
        body = "\n".join("|" + "|".join(map(str, r)) + "|" for r in rows)
        return "\n".join([head, sep, body])

    def get_complete(self, docs):
        passed = set([doc["problem_id"] for doc in docs if doc["passed"]])
        breezy = len(self.breezy.intersection(passed))
        steady = len(self.steady.intersection(passed))
        edgy = len(self.edgy.intersection(passed))
        return breezy, steady, edgy

    def get_stats(self, docs):
        # get recent, frequent, fast and forever.
        latest, best, worst, counts = {}, {}, {}, Counter()
        for d in docs:
            pid = d["problem_id"]
            counts[pid] += 1
            latest[pid] = max(d["created_at"], latest.get(pid, 0))
            if d["passed"]:
                if d["elapsed"] <= 30 * 60 * 60:
                    best[pid] = min(d["elapsed"], best.get(pid, float("inf")))
                else:
                    worst[pid] = min(d["elapsed"], worst.get(pid, float("inf")))
        fast = [
            (
                q.get(id, {}).get("title", ""),
                q.get(id, {}).get("level", ""),
                fmt_secs(tm),
            )
            for id, tm in nsmallest(6, best.items(), key=lambda x: x[1])
        ]
        forever = [
            (
                q.get(id, {}).get("title", ""),
                q.get(id, {}).get("level", ""),
                fmt_secs(tm),
            )
            for id, tm in nlargest(6, worst.items(), key=lambda x: x[1])
        ]
        recent = [
            (
                q.get(id, {}).get("title", ""),
                q.get(id, {}).get("level", ""),
                time_ago(tm),
            )
            for id, tm in nlargest(6, latest.items(), key=lambda x: x[1])
        ]
        frequent = [
            (q.get(id, {}).get("title", ""), q.get(id, {}).get("level", ""), count)
            for id, count in counts.most_common(6)
        ]
        return recent, frequent, fast, forever

    def update_md(self, docs) -> None:
        recent, frequent, fast, forever = self.get_stats(docs)
        latest = self.md_table(["question", "level", "time"], recent)
        popular = self.md_table(["question", "level", "attempts"], frequent)
        best = self.md_table(["question", "level", "best time"], fast)
        worst = self.md_table(["question", "level", "best time"], forever)
        self.query_one("#recent", Markdown).update(latest)
        self.query_one("#frequent", Markdown).update(popular)
        self.query_one("#best", Markdown).update(best)
        self.query_one("#worst", Markdown).update(worst)

    def update_digits(self, ids, values):
        for id, val in zip(ids, values):
            self.animate_digit(id, val)

    def update_progress(self, value):
        self.query_one(ProgressBar).update(progress=value)
