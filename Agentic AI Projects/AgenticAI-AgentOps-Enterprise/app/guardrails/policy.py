from dataclasses import dataclass

@dataclass
class PolicyDecision:
    allowed: bool
    reason: str
    requires_human: bool=False

class PolicyEngine:
    def __init__(self, user_permissions=None):
        self.user_permissions=user_permissions or {"project:read"}

    def input_guardrail(self, text):
        blocked=[
            "ignore all previous instructions",
            "reveal the system prompt",
            "bypass approval"
        ]
        for phrase in blocked:
            if phrase in text.lower():
                return PolicyDecision(False,"Input blocked by prompt-injection guardrail.")
        return PolicyDecision(True,"Input allowed")

    def authorize(self, tool, approval_token):
        missing=[p for p in tool.spec.permissions if p not in self.user_permissions]
        if missing:
            return PolicyDecision(False,f"Missing permissions: {missing}")
        if tool.spec.mutating and approval_token!="APPROVED":
            return PolicyDecision(False,"Human approval required.",True)
        return PolicyDecision(True,"Allowed")

    def output_guardrail(self, text):
        if len(text)>12000:
            return PolicyDecision(False,"Output too long.")
        if "SYSTEM PROMPT:" in text.upper():
            return PolicyDecision(False,"Protected instruction content detected.")
        return PolicyDecision(True,"Output allowed")
