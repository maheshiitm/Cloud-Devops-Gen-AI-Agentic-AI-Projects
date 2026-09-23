from typing import Any, Literal
from pydantic import BaseModel, Field

class UserRequest(BaseModel):
    user_id: str = "demo-user"
    request: str
    approval_token: str | None = None

class Plan(BaseModel):
    objective: str
    steps: list[str]
    requires_human_approval: bool = False
    risk_level: Literal["low","medium","high"] = "low"

class Critique(BaseModel):
    passed: bool
    issues: list[str] = Field(default_factory=list)
    score: float = 0.0

class AgentResponse(BaseModel):
    answer: str
    trace_id: str
    requires_human_approval: bool = False
    audit_events: list[dict[str, Any]] = Field(default_factory=list)
