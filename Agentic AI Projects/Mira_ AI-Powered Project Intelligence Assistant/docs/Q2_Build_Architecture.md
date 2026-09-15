# Q2 — Build Mira: Architecture, Implementation, Cost & Evaluation

## Problem
Nexora PMs/TPMs manage multiple projects and spend substantial manual time on project planning, risk assessment and status reporting. Mira automates these activities while prioritizing data grounding.

## Architecture
Final implementation: **parallel specialist agents + Prompt Template aggregation**.

### Flow
Chat Input → parallel specialist branches → Prompt Template Aggregator → Chat Output

Data grounding is provided through file readers for the project description, timeline, risk matrix and task board.

## Agents
### Project Planner
Produces structured phases, activities and milestones. Must use only supplied project data and return `UNKNOWN`/`INSUFFICIENT DATA` when necessary.

### Risk Assessor
Produces categorized risks, impact and mitigations from the risk dataset. It must not invent generic risks.

### Status Reporter
Counts tasks strictly from the task board and identifies blocked items such as T024. It must not fabricate task statuses.

## Observability
Langfuse captures traces, prompts, model calls, latency and token/cost information under the dedicated Mira-Project-Prod project.

## Evaluation
All twelve baseline scenarios T1–T12 are part of the required evaluation. Initial testing exposed hallucination failures on vague inputs and a task-counting issue. Prompt/system-message guardrails were then strengthened. The supplied completion narrative reports that the post-iteration baseline criteria were passed.

## Cost
The documented estimate uses ~2,000 input and ~1,500 output tokens/run, ~10 runs/user/day and an estimated ~$0.15/user/month under the stated assumptions.

## Production Metrics
1. Accuracy — source-data match for task counts/statuses.
2. Trustworthiness — traceability / hallucination rate.
3. Usefulness — time saved versus the 3–4 hour manual planning baseline.

## Design Decision
The final architecture uses parallel branches because project intelligence can benefit from simultaneous plan, risk and status analysis, followed by centralized synthesis. The Prompt Template also provides a single place to enforce consistent output formatting.
