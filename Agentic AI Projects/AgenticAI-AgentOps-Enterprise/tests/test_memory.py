from app.memory.sqlite_memory import SQLiteMemory

def test_memory(tmp_path):
    m=SQLiteMemory(str(tmp_path/"m.db"))
    m.add("u","episodic","prefers concise reports")
    assert m.search("u","concise")
