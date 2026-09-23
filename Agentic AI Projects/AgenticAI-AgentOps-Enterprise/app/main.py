from fastapi import FastAPI,HTTPException
from .config import settings
from .models import UserRequest,AgentResponse
from .state import AgentState
from .memory.sqlite_memory import SQLiteMemory
from .tools.registry import ToolRegistry
from .tools.project_tools import ProjectLookupTool,RiskUpdateTool
from .harness import AgentHarness
from .context_engine import ContextEngine
from .orchestrator import Orchestrator

app=FastAPI(title="AgenticAI AgentOps Enterprise",version="1.0")
memory=SQLiteMemory(settings.database_path)
registry=ToolRegistry()
registry.register(ProjectLookupTool())
registry.register(RiskUpdateTool())
harness=AgentHarness(registry,memory)
orchestrator=Orchestrator(harness,ContextEngine(memory))

@app.get("/health")
def health():
    return {"status":"ok"}

@app.get("/tools")
def tools():
    return [{"name":t.spec.name,"description":t.spec.description,
             "permissions":t.spec.permissions,"mutating":t.spec.mutating}
            for t in registry.list()]

@app.post("/agent/run",response_model=AgentResponse)
def run_agent(req:UserRequest):
    try:
        state=AgentState(req.request,req.user_id)
        state.approved=req.approval_token=="APPROVED"
        result=orchestrator.run(state)
        return AgentResponse(
            answer=result.answer,trace_id=result.trace_id,
            requires_human_approval=result.awaiting_human,
            audit_events=result.audit_events
        )
    except PermissionError as e:
        raise HTTPException(403,str(e))
    except Exception as e:
        raise HTTPException(500,str(e))
