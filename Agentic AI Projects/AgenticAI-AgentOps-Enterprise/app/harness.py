from .guardrails.policy import PolicyEngine
from .observability.audit import audit
from .observability.tracing import span
from .config import settings


class AgentHarness:
    def __init__(self, registry, memory):
        self.registry = registry
        self.memory = memory

        # Authorization permissions available to this AgentHarness.
        # project:read  -> read project information
        # project:write -> execute project mutations
        #
        # IMPORTANT:
        # project:write permission does NOT bypass Human-in-the-Loop.
        # Mutating requests must still have an approval token.
        self.policy = PolicyEngine(
            {
                "project:read",
                "project:write",
            }
        )

    def intake(self, state):
        """
        Run the input guardrail before any planning or tool execution.
        """

        with span(
            "harness.intake",
            trace_id=state.trace_id,
        ):
            decision = self.policy.input_guardrail(
                state.request
            )

            audit(
                state,
                "input_guardrail",
                allowed=decision.allowed,
                reason=decision.reason,
            )

            if not decision.allowed:
                raise PermissionError(
                    decision.reason
                )

        return state

    def can_continue_tools(self, state):
        """
        Enforce the maximum number of tool calls allowed
        for a single agent execution.
        """

        return (
            state.tool_calls
            < settings.max_tool_calls
        )