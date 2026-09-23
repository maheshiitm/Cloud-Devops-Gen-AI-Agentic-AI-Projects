# AgenticAI AgentOps Enterprise

**Author: Mahesh Zade**

A GitHub-ready Agentic AI reference project covering:

- Agent Harness
- Context Engineering
- Human-in-the-Loop (HITL)
- Tool Design
- Memory Architecture
- Deep Evaluation
- Loop Engineering
- Guardrails & Permissions
- Orchestration Patterns
- Observability & Tracing
- Auditability and regression testing

## Use case

Enterprise Project Intelligence Agent. A user asks about project status, risk or delivery. The runtime plans the work, builds explicit context, calls approved tools, checks policy, uses a bounded critic/repair loop, requests human approval for risky mutations, and produces an auditable result.

## Architecture

```text
User/API
   |
   v
Agent Harness
(auth • policy • budgets • state • audit)
   |
   +--> Context Engineering
   |    task • memory • rules • evidence
   |
   v
Orchestrator
Planner -> Tool Executor -> Critic -> bounded Repair Loop -> Finalizer
   |              |
   |              +--> Tool Registry -> Project DB
   |
   +--> Guardrails / Permissions
   |
   +--> HITL approval for high-risk actions
   |
   +--> Memory Architecture
   |    working • episodic • semantic extension point
   |
   +--> Observability
        traces • metrics • audit • evaluation
```

## Repository

```text
app/
  main.py
  models.py
  state.py
  config.py
  harness.py
  context_engine.py
  orchestrator.py
  memory/
  tools/
  guardrails/
  observability/
evals/
tests/
docs/
prompts/
data/
.github/workflows/
```

## Run

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs`.

Run tests:

```bash
pytest -q
```

Run deep evaluation:

```bash
python -m evals.run_eval
```

## Key design principles

1. The LLM does not own the runtime.
2. Tools are typed, narrow and permissioned.
3. Mutating actions require explicit approval.
4. Retrieved data is untrusted data, not instructions.
5. Loops are bounded by revision and tool budgets.
6. Every important decision gets an audit event.
7. Evaluation is multi-dimensional rather than a single score.
8. Memory has explicit lifecycle and provenance boundaries.

## GitHub project title

**Agentic AI AgentOps Enterprise — Harness, Context Engineering, HITL, Memory, Guardrails, Evaluation & Observability**
