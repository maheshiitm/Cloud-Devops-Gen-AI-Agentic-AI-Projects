import json
from pathlib import Path
from app.state import AgentState

def load_cases():
    return json.loads((Path(__file__).parent/"dataset.json").read_text())

def evaluate_case(case,orchestrator):
    try:
        s=AgentState(case["request"],"eval-user")
        r=orchestrator.run(s)
        blob=str(r.tool_results)+" "+r.answer
        tool_ok=(not case.get("expected_tool")) or any(x["tool"]==case["expected_tool"] for x in r.tool_results)
        contains_ok=all(x.lower() in blob.lower() for x in case.get("expected_contains",[]))
        hitl_ok=(not case.get("expected_human_approval")) or r.awaiting_human
        blocked_ok=not case.get("expected_block",False)
        score=sum([tool_ok,contains_ok,hitl_ok,blocked_ok])/4
        return {"id":case["id"],"score":score,"tool_ok":tool_ok,"contains_ok":contains_ok,"hitl_ok":hitl_ok,"blocked_ok":blocked_ok}
    except PermissionError:
        return {"id":case["id"],"score":1.0 if case.get("expected_block") else 0.0,"blocked_ok":bool(case.get("expected_block"))}
    except Exception as e:
        return {"id":case["id"],"score":0.0,"error":str(e)}
