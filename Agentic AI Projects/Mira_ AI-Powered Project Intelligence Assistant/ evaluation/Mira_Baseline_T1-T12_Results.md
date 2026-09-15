# Mira Baseline Evaluation — T1 to T12

> **Evidence note:** Final statuses below reflect the post-iteration completion narrative in the supplied playbook. The document also contains an earlier table showing initial failures; the corrected T1–T12 runs should be retained as Langfuse evidence for auditability.

| ID | Scenario | Final status | Key criterion |
|---|---|---|---|
| T1 | Detailed project plan | PASS | Phases, milestones, timeline |
| T2 | Vague chatbot plan | PASS after fix | Insufficient data / scope, timeline, team size |
| T3 | Detailed risk assessment | PASS | Categorized project-relevant risks |
| T4 | Vague risk request | PASS after fix | Insufficient data / project details |
| T5 | Sprint 3 status report | PASS | Tasks by status; actual task names |
| T6 | Status request with no data | PASS after fix | No task data available |
| T7 | Top 3 risks | PASS | Actual risk IDs/data |
| T8 | Blocked / at-risk tasks | PASS | T024 Security review — BLOCKED |
| T9 | 2-week project, no details | PASS after fix | Ask for scope/goals/deliverables |
| T10 | Current task counts | PASS after fix | Counts must match raw board |
| T11 | Next 2 weeks milestones | PASS | Actual timeline milestones |
| T12 | Sprint 2 stakeholder email | PASS | Sprint 2 tasks only; professional |

## Initial failures documented in the playbook
T2, T4, T6, T9 and T10 were initially identified as failing because of hallucinated content or incorrect task counts. The documented remediation was to strengthen each agent's System Message with explicit grounding and Vague Input Rules.
