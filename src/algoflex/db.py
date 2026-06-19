from tinydb import TinyDB, Query
from platformdirs import user_data_dir
from pathlib import Path
from time import time 

_db_instance = None
KV = Query()


def get_db():
    global _db_instance
    if _db_instance is None:
        app_data_dir = Path(user_data_dir("algoflex"))
        app_data_dir.mkdir(parents=True, exist_ok=True)
        path = Path(app_data_dir, "attempts.json")
        _db_instance = TinyDB(path=path)
    return _db_instance

attempts = get_db()
drafts = get_db().table("drafts")

def save_draft(problem_id, code, elapsed):
    drafts.upsert(
        {
            "problem_id": problem_id,
            "code": code, 
            "elapsed": elapsed,
            "updated_at": time(),
        },
        KV.problem_id == problem_id,
    )

def load_draft(problem_id):
    return drafts.get(KV.problem_id == problem_id)

def delete_draft(problem_id):
    drafts.remove(KV.problem_id == problem_id)