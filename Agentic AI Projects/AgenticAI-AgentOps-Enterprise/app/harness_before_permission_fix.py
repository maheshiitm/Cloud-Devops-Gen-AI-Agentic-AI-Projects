from .guardrails.policy import PolicyEngine
from .observability.audit import audit
from .observability.tracing import span
from .config import settings

class AgentHarness:
    def __init__(self,registry,memory):
        self.registry=registry
        self.memory=memory
        self.policy=PolicyEngine()

    def intake(self,state):
        with span("harness.intake",trace_id=state.trace_id):
            d=self.policy.input_guardrail(state.request)
            audit(state,"input_guardrail",allowed=d.allowed,reason=d.reason)
            if not d.allowed:
                raise PermissionError(d.reason)
        return state

    def can_continue_tools(self,state):
        return state.tool_calls < settings.max_tool_calls
