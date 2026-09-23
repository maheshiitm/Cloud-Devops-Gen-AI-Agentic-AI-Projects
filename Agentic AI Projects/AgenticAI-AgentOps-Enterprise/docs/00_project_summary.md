# Capability Matrix

| Capability | Implementation |
|---|---|
| Agent Harness | app/harness.py |
| Context Engineering | app/context_engine.py |
| Human in the Loop | app/orchestrator.py + policy |
| Tool Design | app/tools |
| Memory Architecture | app/memory |
| Deep Evaluation | evals |
| Loop Engineering | bounded critic/repair loop |
| Guardrails | app/guardrails |
| Permissions | ToolSpec.permissions |
| Orchestration | app/orchestrator.py |
| Observability | app/observability |
| Tracing | trace_id + spans |
| Auditability | structured audit events |
