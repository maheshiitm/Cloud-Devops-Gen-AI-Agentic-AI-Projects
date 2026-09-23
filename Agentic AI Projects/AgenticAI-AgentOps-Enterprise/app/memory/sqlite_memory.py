import sqlite3, json
from datetime import datetime, timezone
from .base import MemoryStore

class SQLiteMemory(MemoryStore):
    def __init__(self, path="agent_memory.db"):
        self.path = path
        with sqlite3.connect(path) as db:
            db.execute(
                "CREATE TABLE IF NOT EXISTS memories("
                "id INTEGER PRIMARY KEY,user_id TEXT,memory_type TEXT,"
                "content TEXT,metadata TEXT,created_at TEXT)"
            )
            db.commit()

    def add(self, user_id, memory_type, content, metadata=None):
        with sqlite3.connect(self.path) as db:
            db.execute(
                "INSERT INTO memories(user_id,memory_type,content,metadata,created_at) VALUES(?,?,?,?,?)",
                (user_id,memory_type,content,json.dumps(metadata or {}),
                 datetime.now(timezone.utc).isoformat())
            )
            db.commit()

    def get_recent(self, user_id, limit=10):
        with sqlite3.connect(self.path) as db:
            rows=db.execute(
                "SELECT memory_type,content,metadata,created_at FROM memories "
                "WHERE user_id=? ORDER BY id DESC LIMIT ?",(user_id,limit)
            ).fetchall()
        return [{"type":a,"content":b,"metadata":c,"created_at":d} for a,b,c,d in rows]

    def search(self, user_id, query, limit=5):
        with sqlite3.connect(self.path) as db:
            rows=db.execute(
                "SELECT memory_type,content,metadata,created_at FROM memories "
                "WHERE user_id=? AND lower(content) LIKE ? ORDER BY id DESC LIMIT ?",
                (user_id,"%"+query.lower()+"%",limit)
            ).fetchall()
        return [{"type":a,"content":b,"metadata":c,"created_at":d} for a,b,c,d in rows]
