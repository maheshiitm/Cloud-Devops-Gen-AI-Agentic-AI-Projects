# Q2 --- Build CalendarMate: Implementation & Evaluation

## 1. Design

CalendarMate implements a Router/Dispatcher-style multi-agent workflow
in Langflow.

### Functionality Mapping

  -----------------------------------------------------------------------
  Capability        Agent             Tool in validated Expected behavior
                                      graph             
  ----------------- ----------------- ----------------- -----------------
  Daily briefing    Scheduler Agent   Mock Calendar     Summarize
                                      Tool              schedule and
                                                        avoid fabrication

  Smart scheduling  Scheduler Agent   Mock Calendar     Check
                                      Tool              availability,
                                                        handle conflicts,
                                                        create event in
                                                        controlled test
                                                        environment

  Email             Email Agent       Mock Gmail Tool   Summarize and
  summarization                                         prioritize
                                                        returned emails

  Meeting follow-up Follow-Up Agent   None              Draft only from
                                                        supplied meeting
                                                        details
  -----------------------------------------------------------------------

## 2. Agent Design

### Scheduler Agent

-   Briefing + scheduling responsibility.
-   Uses grounding rules.
-   Uses calendar tool before scheduling.
-   Handles ambiguity and conflicts.

### Email Agent

-   Reads/summarizes email data.
-   Separates action-required and FYI.
-   Does not fabricate or send messages.

### Follow-Up Agent

-   Creates meeting summary and action-item output from supplied notes.
-   Does not invent action items, deadlines, or assignees.
-   Requests missing information.

## 3. Tool Selection Rationale

The mock tools were used for deterministic evaluation. The exported
workflow also contains Google Calendar/Gmail API components, but those
live components are not connected in the validated graph.

This means the baseline evidence demonstrates the agent/tool
orchestration pattern under controlled inputs; live API execution must
be validated separately before production claims.

## 4. Observability

Langfuse was configured for tracing. Supplied evidence documents trace
execution, token usage, latency, and cost.

## 5. Baseline Evaluation

The supplied results report 12/12 baseline tests passed.

  Test Group   Tests                     Result
  ------------ ------------------------- --------------
  Briefing     T1, T2, T10, T12          Passed
  Scheduling   T3, T4, T5, T6, T9, T11   Passed
  Email        T7, T8                    Passed
  Total        T1--T12                   12/12 passed

## 6. Edge Cases

The supplied evaluation artifacts also document: - Empty calendar day. -
Past-date scheduling. - Vague email request.

## 7. Prompt Modification Findings

The supplied results report that adding explicit grounding rules reduced
an early failure mode involving inferred meeting titles.

The routing instructions were also tightened to reduce misrouting
between scheduling and follow-up requests.

## 8. Production Metrics

Recommended metrics: 1. Meeting logistics time saved. 2.
Double-booking/conflict rate. 3. Task completion latency. 4. Baseline
evaluation pass rate. 5. Hallucination/unsupported-content rate. 6. Cost
per user per day.

## 9. Acceptance Criteria

-   12/12 baseline tests pass.
-   No fabricated meetings, attendees, or email content.
-   Required tool calls occur for applicable tasks.
-   Trace data is available in Langfuse.
-   Cost and latency remain within target ranges.
