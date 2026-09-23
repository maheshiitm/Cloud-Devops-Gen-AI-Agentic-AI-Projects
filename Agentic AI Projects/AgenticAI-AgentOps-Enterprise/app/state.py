from dataclasses import dataclass, field
import uuid

@dataclass
class AgentState:
    request: str
    user_id: str
    trace_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    plan: object | None = None
    context: list = field(default_factory=list)
    tool_results: list = field(default_factory=list)
    critique: object | None = None
    answer: str = ""
    revision_count: int = 0
    tool_calls: int = 0
    awaiting_human: bool = False
    approved: bool = False
    audit_events: list = field(default_factory=list)
