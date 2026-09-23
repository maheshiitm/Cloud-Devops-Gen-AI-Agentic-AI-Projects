from datetime import datetime, timezone

def audit(state, event, **details):
    state.audit_events.append({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "trace_id": state.trace_id,
        "event": event,
        "details": details
    })
