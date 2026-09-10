# CalendarMate --- AI-Powered Productivity Assistant

**Agentic AI Capstone Project**\
**Submitted by:** Mahesh P Zade\
**Organization context:** ServionIQ Solutions\
**Workflow platform:** Langflow\
**LLM in validated export:** OpenAI `gpt-4o-mini`\
**Observability:** Langfuse

## 1. Project Overview

CalendarMate is an Agentic AI productivity assistant designed to reduce
the operational overhead faced by PMs, TPMs, and senior ICs who manage
high volumes of meetings and meeting-related email.

The capstone problem statement describes a typical workload of **8--14
meetings/day, 3--5 calendars to cross-reference, 60+ emails/day, and
approximately 2 hours/day spent on meeting logistics, scheduling, and
email triage**.

CalendarMate addresses this problem through intent-based routing to
specialist agents for scheduling, email triage, and meeting follow-up,
with grounding rules intended to prevent fabricated meetings, attendees,
or email content.

## 2. Problem Statement

ServionIQ PMs/TPMs and senior ICs spend significant time switching
between calendars and inboxes. Manual availability checks can cause
double-bookings, while meeting action items and email follow-ups can be
missed.

The goal is to automate repetitive productivity workflows while keeping
actions grounded in available tool data and requiring clarification when
critical information is missing.

## 3. Objectives

-   Provide a consolidated briefing of calendar activity.
-   Support natural-language scheduling and conflict handling.
-   Summarize and prioritize email.
-   Generate meeting follow-up content from supplied meeting
    information.
-   Use an Agentic AI routing architecture.
-   Add observability with Langfuse.
-   Evaluate the workflow against all 12 baseline test cases plus
    additional edge cases.
-   Document cost, production metrics, security considerations, and
    future improvements.

## 4. Architecture at a Glance

The validated exported flow uses a **Router/Dispatcher-style design**
implemented with three custom route-filter components. A single Chat
Input feeds the Scheduler, Email, and Follow-Up route filters. Only the
matching route continues to its specialist agent.

``` text
User
  |
  v
Chat Input
  |
  +--> Route: Scheduler --> Scheduler Agent --> Mock Calendar Tool --> Chat Output
  |
  +--> Route: Email -----> Email Agent -----> Mock Gmail Tool ------> Chat Output
  |
  +--> Route: Follow-Up -> Follow-Up Agent -------------------------> Chat Output
                                |
                                +--> Langfuse observes execution
```

> **Implementation accuracy note:** The exported JSON also contains
> Google Calendar Read, Google Calendar Write, and Gmail Read
> components. Those components are present in the export but are not
> connected to the validated execution path represented by the current
> graph. The documented baseline evidence therefore represents the
> mock-tool validation path. This distinction is intentionally
> documented rather than claiming live API execution that is not
> evidenced by the export.

See [`docs/architecture.md`](docs/architecture.md) and
[`docs/architecture-diagram.png`](docs/architecture-diagram.png).

## 5. Agent Design

  -----------------------------------------------------------------------
  Agent                   Responsibility          Connected tool in
                                                  validated graph
  ----------------------- ----------------------- -----------------------
  Scheduler Agent         Briefing and            Mock Calendar Tool
                          scheduling;             
                          availability/conflict   
                          handling                

  Email Agent             Unread/important email  Mock Gmail Tool
                          summarization and       
                          prioritization          

  Follow-Up Agent         Draft meeting follow-up No connected tool in
                          summary/action items    exported graph
  -----------------------------------------------------------------------

The assignment allows agents to be combined, split, or renamed. In this
implementation, briefing behavior is handled by the Scheduler Agent
rather than a separate Briefing Agent.

## 6. Core and Extended Capabilities

### Core Capabilities

1.  **Daily Briefing**
    -   Calendar summary
    -   Meeting times
    -   Conflict awareness
    -   Focus-oriented response
2.  **Smart Scheduling**
    -   Natural-language scheduling requests
    -   Availability checking
    -   Conflict warning
    -   Alternative slot suggestion
    -   Event creation in the validated mock environment
3.  **Email Summarization**
    -   Unread/important email summarization
    -   Action-required vs. FYI separation
    -   Sender/subject awareness
    -   No fabricated email content

### Selected Extended Capability

**Meeting Follow-Up Generator** - Generates a professional follow-up
based only on information provided. - Does not invent action items,
deadlines, or assignees. - Requests missing information when needed.

## 7. Orchestration Pattern and Rationale

**Selected pattern: Router / Dispatcher.**

CalendarMate receives heterogeneous requests. A scheduling request
should not run an email workflow, and an email request should not run
calendar logic. The route filters therefore identify the relevant intent
and allow only the appropriate specialist branch to continue.

This reduces unnecessary model/tool execution and keeps each agent's
responsibility focused.

## 8. Technology Stack

  -----------------------------------------------------------------------
  Area                                Technology
  ----------------------------------- -----------------------------------
  Agent/workflow platform             Langflow

  LLM                                 OpenAI `gpt-4o-mini`

  Observability                       Langfuse

  Workflow export                     JSON

  Agent tools in validated test path  Custom Mock Calendar / Mock Gmail
                                      components

  API components present in export    Google Calendar Read/Write, Gmail
                                      Read

  Authentication components           Google OAuth credential fields in
                                      API nodes
  -----------------------------------------------------------------------

## 9. Prompt Engineering

The agents use explicit grounding rules. Key safeguards include:

-   Do not invent meetings, attendees, or email content.
-   Check calendar availability before scheduling.
-   Ask for missing or ambiguous scheduling information.
-   Warn about conflicts and unusual scheduling requests.
-   Keep email processing within the Email Agent's scope.
-   Do not invent follow-up action items, deadlines, or assignees.

Prompt files are available under `docs/prompts/`.

## 10. Evaluation and Observability

The supplied evaluation artifacts document **12/12 baseline tests
passed** with no hallucination anomalies reported.

The baseline dataset covers:

-   T1--T2: briefing
-   T3--T6: scheduling and edge cases
-   T7--T8: email
-   T9: missing information
-   T10: weekly conflict detection
-   T11: scheduling conflict
-   T12: specific-day briefing

Additional edge cases documented in the supplied results include
empty-calendar handling, past-date scheduling, and vague email requests.

Langfuse evidence reports: - \~2,890 tokens/execution in a sample
trace - \~4.0 seconds total latency - \~1.28 seconds
time-to-first-token - observed sample cost of \~\$0.000286/execution

See [`docs/baseline-test-results.md`](docs/baseline-test-results.md) and
`evidence/`.

## 11. Cost Analysis

Using the observed Langfuse cost of approximately **\$0.000286 per
execution** as the empirical figure:

-   15 interactions/day ≈ **\$0.00429/user/day**
-   30 interactions/day ≈ **\$0.00858/user/day**
-   30 interactions/day × 20 business days ≈ **\$0.1716/user/month**

The exact production bill will depend on current provider pricing,
prompt length, output length, tool usage, and infrastructure. The
empirical Langfuse figure should therefore be treated as the evaluation
measurement, not a universal fixed price.

See [`docs/cost-analysis.md`](docs/cost-analysis.md).

## 12. Security and Privacy

The intended production design should use OAuth2 for Google services,
least-privilege scopes, secure secret storage, data minimization, and
auditable traces.

The current validated capstone path uses mock tools, so live production
credential handling is not claimed as part of the executed baseline
path.

Recommended production controls: - Never commit API keys or OAuth
secrets. - Store secrets in environment variables or a secret manager. -
Use least-privilege Google scopes. - Add approval before high-impact
calendar/email write actions. - Review Langfuse retention and
sensitive-data settings.

## 13. Repository Structure

``` text
CalendarMate/
├── README.md
├── .gitignore
├── GITHUB_UPLOAD_GUIDE.md
├── SUBMISSION_CHECKLIST.md
├── SUBMISSION_SUMMARY.md
├── CALENDARMATE_CAPSTONE-JSON.json
├── PRD.md
├── langflow-to-start-and-docker.txt
├── docs/
│   ├── business-case.md
│   ├── program-charter.md
│   ├── architecture.md
│   ├── architecture-diagram.png
│   ├── q2-build-and-evaluation.md
│   ├── cost-analysis.md
│   ├── reflection.md
│   ├── baseline-test-results.md
│   └── prompts/
│       ├── briefing-agent-prompt.md
│       ├── scheduler-agent-prompt.md
│       ├── email-agent-prompt.md
│       └── follow-up-agent-prompt.md
├── images/
│   ├── architecture-diagram.png
│   ├── langfuse-report-page-06.png
│   ├── langfuse-report-page-07.png
│   └── langfuse-report-page-08.png
└── evidence/
    ├── CalendarMate_Langfuse_Traces_Report.pdf
    └── CalendarMate_12_Test_Cases_Langfuse.pptx
```

## 14. Setup

1.  Install/start Langflow.
2.  Import `CALENDARMATE_CAPSTONE-JSON.json`.
3.  Configure provider credentials only if using the live API
    components.
4.  Configure Langfuse credentials if tracing is enabled.
5.  Run the workflow in the Langflow Playground.
6.  Validate against the baseline dataset.
7.  Review traces in Langfuse.

**Important:** Never commit real API keys, refresh tokens, or client
secrets.

## 15. Example Requests

``` text
What does my day look like today?
Give me a summary of my meetings for tomorrow.
Schedule a 30-minute meeting with sarah@company.com tomorrow at 2pm.
Summarize my unread emails.
What emails need my attention today?
Book a meeting but I forgot with whom.
Do I have any conflicts this week?
Follow up on the pending action items from last week's project review meeting.
```

## 16. Limitations and Known Submission Risk

The exported graph is a strong capstone prototype, but the current JSON
shows the validated agents connected to **mock Calendar/Gmail tools**,
while live Google API nodes are present but not connected.

Therefore:

-   The baseline results demonstrate workflow behavior and tool-calling
    logic in a controlled test environment.
-   They should not be described as live Google Calendar/Gmail
    production transactions.
-   Before a production claim, connect and validate the live API
    components and capture fresh traces.

## 17. Future Enhancements

-   Connect and validate live Google Calendar/Gmail APIs.
-   Add human approval before event creation or email sending.
-   Add RAG for historical meeting/document grounding.
-   Add richer conflict-resolution logic.
-   Add weekly digest functionality.
-   Add user feedback loops and evaluation dashboards.
-   Optimize prompts and token consumption.
-   Add production authentication/secret-management controls.

## 18. Author

**Mahesh P Zade**\
Applied Agentic AI Capstone Project

## 19. Acknowledgment

I sincerely thank **Gautam Muthukumar** for his valuable guidance,
continuous support, and encouragement throughout the CalendarMate
Capstone Project.

I also thank the **Interview Kickstart Team** for providing the learning
platform, resources, mentorship, and opportunity that enabled me to
complete this Agentic AI Capstone Project.

------------------------------------------------------------------------

**Thank You**\
**Mahesh P Zade**


## Evidence Naming Note

The `images/` folder contains rendered evidence pages from the supplied Langfuse report. The exact live Langflow canvas screenshot is **not included in the supplied source package as a standalone image**; the repository should include the original Langflow canvas screenshot if your evaluator explicitly requires it.
