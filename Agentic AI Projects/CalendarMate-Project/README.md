# CalendarMate — AI-Powered Productivity Assistant

Multi-agent assistant that collapses a PM/TPM's ~2 hrs/day of meeting logistics, scheduling,
and email triage. Built as a **single Langflow flow** with a Router orchestrator over four
specialist agents, grounded in live Google Calendar + Gmail data, instrumented end-to-end
with **Langfuse**.

Capstone: *Applied Agentic AI for PMs/TPMs — CalendarMate*.

## Planning artifacts

| Doc | Path |
| --- | --- |
| PRD | `../_bmad_outputs/planning-artifacts/prds/prd-calendarmate-2026-09-03/prd.md` |
| Architecture spine (AD-1…AD-13) | `../_bmad_outputs/planning-artifacts/architecture/architecture-calendarmate-2026-09-03/ARCHITECTURE-SPINE.md` |
| Solution design (full technical design) | `.../architecture-calendarmate-2026-09-03/solution-design.md` |
| Epics & stories (7 epics, 42 stories) | `../_bmad_outputs/planning-artifacts/epics.md` |
| **Build guide (start here)** | `docs/langflow-build-guide.md` |

## Repo layout

```
calendarmate/
  infra/     docker-compose.yml, .env.example   — local Langflow + Langfuse stack
  shared/    README.md                          — the 7 shared helper contracts (AD-2,8,9,11,13)
  prompts/   grounding_preamble.md + 5 agent system prompts (AD-3, AD-11, AD-12)
  eval/      dataset_baseline.json (T1–T12), dataset_edgecases.json (9), results/
  flows/     calendarmate.flow.json             — exported Langflow flow (secrets scrubbed) [add on build]
  docs/      langflow-build-guide.md, architecture.md, solution-design.md, diagram.* [add drawn diagram]
  screenshots/  canvas, in-action, Langfuse traces [add on build]
```

## Quick start

```bash
cd infra
cp .env.example .env         # fill in every value (openssl rand -hex 32 for secrets)
docker compose up -d
```

- Langflow  http://127.0.0.1:7860  ·  Langfuse  http://127.0.0.1:3000
- After first Langfuse login, copy the project keys into `.env` and `docker compose up -d` again.
- Then follow `docs/langflow-build-guide.md` step by step (ordered by the epic backlog).

## Architecture in one paragraph

One Langflow flow. `Chat Input` → **Orchestrator** (classifies intent into
`briefing | scheduling | email | follow_up | out_of_scope | needs_clarification`, extracts
`params`, never calls a tool) → exactly one **worker** sub-graph
(`retrieve → reason → (approve) → act → format`) → one shared **Response Formatter** →
`Chat Output`. Mutating workers (Scheduler, Follow-Up) use a **two-phase write**: propose
(preview + `approval.state=pending`, nothing written) then commit (only on an affirmative
user turn, which adopts the pending proposal's `request_id`) via the Langflow 1.11
Human-in-the-Loop checkpoint node. Every request = one Langfuse trace with a fixed span set.
See `docs/langflow-build-guide.md` and the architecture spine.

## Submission checklist (capstone Q2)

- [ ] `flows/calendarmate.flow.json` exported, secrets scrubbed
- [ ] Architecture diagram in `docs/` (Excalidraw/draw.io) — blueprint is the spine's container view
- [ ] `eval/results/` — all 12 baseline inputs (T1–T12) with output + pass/fail + trace link
- [ ] ≥5 edge cases documented (`eval/dataset_edgecases.json` has 9)
- [ ] `eval/prompt_iteration.md` — one before/after experiment
- [ ] Langfuse dashboards: SM-1, SM-2, SM-4 alert, SM-6, SM-7, SM-8
- [ ] Cost per user per day measured (replaces PRD §13.3 floor)
- [ ] Screenshots: workflow canvas, CalendarMate in action, Langfuse traces
- [ ] README + this repo pushed to GitHub