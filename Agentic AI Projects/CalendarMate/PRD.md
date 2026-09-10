# Product Requirements Document (PRD)
## CalendarMate — AI-Powered Productivity Assistant

**Author:** Mahesh Zade, Technical Program Manager
**Organization:** ServionIQ Solutions
**Status:** Capstone Build — Pilot Ready
**Last Updated:** September 2026

---

## 1. Problem Statement

ServionIQ's PMs, TPMs, and senior ICs manage a heavy operational load across professional-services delivery:

- 8–14 meetings/day across engineering, product, design, and client teams
- 3–5 team calendars to cross-reference before scheduling anything
- 30–45 minutes every morning spent figuring out what's happening today
- Frequent double-bookings due to manual availability checks
- Action items from meetings are discussed but rarely tracked systematically
- 60+ emails/day, many meeting-related (invites, reschedules, FYIs, follow-ups)
- No consolidated view of the day — constant switching between calendar, email, Slack, docs

**Net effect:** ~2 hours/day per PM/TPM lost to meeting logistics, scheduling, and email triage instead of high-value delivery work.

---

## 2. Goal

Build an AI-powered assistant that removes the manual, repetitive parts of calendar and inbox management, so PMs/TPMs reclaim time for client-facing and strategic work — without adding operational risk (no invented meetings, no unconfirmed bookings, no fabricated email content).

---

## 3. Target Users

| User | Primary Need |
|---|---|
| PM/TPM | Daily briefing, conflict-free scheduling, less time in inbox |
| Senior IC | Fast context on the day, meeting follow-through without manual note-taking |
| ServionIQ leadership | Utilization gains without headcount growth; auditable, low-risk automation |

---

## 4. Scope

### 4.1 Core Capabilities (in scope, required)

| Capability | Description |
|---|---|
| **Daily Briefing** | Consolidated summary of today's meetings (times, attendees), conflicts, priority emails, suggested focus plan. |
| **Smart Scheduling** | Accepts natural-language requests, checks availability, proposes open slots, creates the event with a Google Meet link once confirmed. |
| **Email Summarization** | Groups unread/recent emails by urgency or topic; separates action-required from FYI. |

### 4.2 Extended Capability (in scope, selected)

| Capability | Description |
|---|---|
| **Meeting Follow-Up Generator** | After a meeting, generates a follow-up email with action items and sends it to attendees. |

### 4.3 Out of Scope (for this release)

- Human-in-the-Loop approval gating (planned Week 1 of post-pilot improvement plan)
- RAG grounding against historical docs/communications (planned Week 2)
- Fine-tuning any agent on evaluation data
- Attendee research / Weekly digest capabilities
- Mobile-native UI (chat-based interface only for this release)

---

## 5. Functional Requirements

| ID | Requirement |
|---|---|
| FR-1 | System must classify each incoming request into Briefing, Scheduling, Email, or Follow-Up intent and route to exactly one specialist agent. |
| FR-2 | Scheduler Agent must check calendar availability before proposing or creating any event. |
| FR-3 | Scheduler Agent must never create an event when required details (time, attendee) are missing or ambiguous — it must ask for clarification instead. |
| FR-4 | Scheduler Agent must detect conflicts (including same-time-as-existing-meeting cases) and warn the user with alternative slots. |
| FR-5 | Scheduler Agent must flag unusual scheduling requests (e.g., weekends, very early/late hours) and request confirmation. |
| FR-6 | Email Agent must separate action-required emails from FYI emails and must not fabricate email content. |
| FR-7 | Briefing Agent must reflect only real calendar/email data returned by tool calls — never invented meetings. |
| FR-8 | Follow-Up Agent must generate action items and a summary after a meeting and route it to attendees. |
| FR-9 | Every agent response must be traceable end-to-end in the observability tool (latency, tokens, tool calls). |

---

## 6. Non-Functional Requirements

| Category | Requirement |
|---|---|
| **Grounding / Hallucination Control** | 0% hallucination rate on baseline test dataset (T1–T12); all outputs must be traceable to a tool call. |
| **Latency** | Target end-to-end response time under ~5 seconds per request. |
| **Cost** | Target cost per user per day under $0.05 (current measured: ~$0.0075/day, ~$0.20–0.25/month/user). |
| **Observability** | 100% of agent runs traced (latency, token count, tool calls) via Langfuse. |
| **Security** | OAuth2-based access to Calendar/Email APIs; data minimization for client-sensitive content. |

---

## 7. System Design Summary

- **Orchestration Pattern:** Router / Dispatcher — a Chat Input fans out to three parallel route-filter nodes (Route: Scheduler, Route: Email, Route: Follow-Up) that classify intent and dispatch to the matching specialist agent.
- **Agents:** Scheduler Agent, Email Agent, Follow-Up Agent (all gpt-4o-mini).
- **Tools:** Mock Calendar Tool, Mock Gmail Tool (for grounded testing), with live Google Calendar Read/Write and Gmail Read tools available for production use.
- **Platform:** Langflow (workflow), Langfuse (observability).

Full diagram: [`architecture/Architecture_Diagram.md`](../architecture/Architecture_Diagram.md)

---

## 8. Success Metrics

| Metric | Target | How Measured |
|---|---|---|
| Meeting logistics time saved | ≥ 60 min/day/user | Self-reported time diaries, pre/post pilot |
| Double-booking / conflict rate | ≥ 50% reduction | Calendar audit vs. baseline |
| Task completion latency | < 5 sec median | Langfuse trace data |
| Baseline test pass rate | 12/12 (100%) | Documented test run against Problem Statement dataset |
| Hallucination rate | 0% | Manual review of each traced output |

---

## 9. Rollout Plan

| Phase | Duration | Scope |
|---|---|---|
| Phase 1 — Pilot | Weeks 1–2 | 10 TPMs, mock tools + live Calendar/Email APIs, close monitoring via Langfuse |
| Phase 2 — Expansion | Weeks 3–4 | Expand to 50 TPMs after reviewing pilot telemetry for latency/accuracy |
| Phase 3 — Hardening | Post-rollout | Add Human-in-the-Loop approval (Week 1 of improvement plan) and RAG grounding (Week 2) |

---

## 10. Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Agent books/sends without user confirmation | FR-3/FR-5 enforce clarification and confirmation on ambiguous or unusual requests |
| Hallucinated meetings/emails | Strict grounding rules in every system prompt; tool-call-only responses; 0% hallucination target verified per release |
| Misrouted requests | Explicit per-route keyword/intent examples in Router prompts; monitored via Langfuse |
| Cost creep at scale | Per-user daily cost tracked via Langfuse token metrics; gpt-4o-mini selected specifically for low per-run cost |
| Data privacy (client-sensitive calendar/email content) | OAuth2 scoped access, data minimization principles, enterprise compliance review before Phase 2 |

---

## 11. Open Questions

- Should Human-in-the-Loop approval be mandatory for all event creation, or only for external/multi-attendee meetings?
- What is the acceptable false-positive rate for conflict detection before it becomes noisy for users?
- Does Phase 2 expansion require per-team calendar permission scoping, or is org-wide OAuth sufficient?
