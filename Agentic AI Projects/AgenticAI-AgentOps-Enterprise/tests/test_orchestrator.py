from app.state import AgentState
from app.memory.sqlite_memory import SQLiteMemory
from app.tools.registry import ToolRegistry
from app.tools.project_tools import ProjectLookupTool,RiskUpdateTool
from app.harness import AgentHarness
from app.context_engine import ContextEngine
from app.orchestrator import Orchestrator

def test_e2e(tmp_path):
    m=SQLiteMemory(str(tmp_path/"m.db"))
    r=ToolRegistry()
    r.register(ProjectLookupTool()); r.register(RiskUpdateTool())
    o=Orchestrator(AgentHarness(r,m),ContextEngine(m))
    s=o.run(AgentState("What is P1001 status?","u"))
    assert "Cloud Migration" in s.answer
