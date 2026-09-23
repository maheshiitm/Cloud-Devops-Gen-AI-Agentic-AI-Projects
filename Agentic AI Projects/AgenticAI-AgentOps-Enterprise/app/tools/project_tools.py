import json
from pathlib import Path
from .base import BaseTool, ToolSpec

DATA=Path(__file__).resolve().parents[2]/"data"/"projects.json"

class ProjectLookupTool(BaseTool):
    spec=ToolSpec(
        name="project_lookup",
        description="Read project status, owner, milestone, progress and risk.",
        permissions=["project:read"], mutating=False
    )
    def run(self, arguments):
        projects=json.loads(DATA.read_text())
        pid=arguments.get("project_id")
        name=(arguments.get("name") or "").lower()
        return [p for p in projects if (pid and p["id"]==pid) or (name and name in p["name"].lower())]

class RiskUpdateTool(BaseTool):
    spec=ToolSpec(
        name="risk_update",
        description="Update project risk. Requires project:write and human approval.",
        permissions=["project:write"], mutating=True
    )
    def run(self, arguments):
        return {"status":"simulated","message":"No real system was modified.","arguments":arguments}
