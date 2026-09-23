from app.tools.project_tools import ProjectLookupTool

def test_lookup():
    r=ProjectLookupTool().run({"project_id":"P1001"})
    assert r[0]["name"]=="Cloud Migration"
