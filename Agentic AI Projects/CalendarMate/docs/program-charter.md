# Q3 --- Program Charter

## CalendarMate --- AI-Powered Productivity Assistant

**Project Owner:** Mahesh P Zade\
**Sponsor:** CTO / ServionIQ Solutions context\
**Program Type:** Applied Agentic AI Capstone

## 1. Vision

Enable PMs, TPMs, and senior ICs to spend less time on repetitive
meeting logistics, scheduling, and email triage and more time on
strategic, client-facing, and delivery-focused work.

## 2. Purpose

Build and evaluate an Agentic AI productivity assistant that can
understand natural-language productivity requests, route them to
specialist agents, use tools where appropriate, and produce grounded
responses.

## 3. Objectives

-   Implement a Router/Dispatcher-style multi-agent workflow.
-   Implement scheduling/briefing, email, and follow-up specialist
    behaviors.
-   Add grounding rules to reduce hallucinations.
-   Add tool calling for controlled calendar and email operations.
-   Integrate Langfuse observability.
-   Execute the 12 baseline tests and additional edge cases.
-   Document cost and production evaluation metrics.

## 4. Scope

### In Scope

-   Langflow workflow.
-   Scheduler/Briefing Agent.
-   Email Agent.
-   Follow-Up Agent.
-   Route filters for intent-based dispatch.
-   Mock Calendar and Mock Gmail tools for controlled baseline testing.
-   Google Calendar/Gmail components included in the workflow export.
-   Langfuse observability.
-   Baseline and edge-case evaluation.
-   Documentation and submission artifacts.

### Out of Scope for the validated capstone path

-   Production deployment to 50 real users.
-   Verified live end-to-end Google Calendar/Gmail transactions in the
    submitted baseline path.
-   Fine-tuning.
-   RAG over historical organizational documents.
-   Mobile-native application.
-   Autonomous high-impact actions without approval.

## 5. Architecture Decision

**Router / Dispatcher** is selected because requests are heterogeneous.
The route filters allow a scheduling request to continue to the
Scheduler Agent, email requests to the Email Agent, and follow-up
requests to the Follow-Up Agent.

## 6. Stakeholders

  -----------------------------------------------------------------------
  Stakeholder                         Responsibility / Interest
  ----------------------------------- -----------------------------------
  CTO / Sponsor                       Business sponsorship and strategic
                                      alignment

  Mahesh P Zade                       Project owner / AI PM-TPM

  PMs / TPMs                          Primary users

  Senior ICs                          Secondary users

  ML/AI engineering                   Technical implementation support

  Google Workspace administration     API/authentication support for
                                      production
  -----------------------------------------------------------------------

## 7. Key Deliverables

-   Workflow JSON export.
-   Architecture diagram.
-   Architecture write-up.
-   Business case.
-   Program charter.
-   Reflection and next steps.
-   Baseline test results for T1--T12.
-   Langfuse observability evidence.
-   Cost analysis.
-   Slide deck.
-   GitHub repository with README.

## 8. Timeline

  -----------------------------------------------------------------------
  Phase                   Activity                Outcome
  ----------------------- ----------------------- -----------------------
  Phase 1                 Problem definition and  Problem and success
                          requirements            criteria

  Phase 2                 Architecture and agent  Router pattern + agent
                          design                  responsibilities

  Phase 3                 Langflow implementation Connected workflow

  Phase 4                 Tooling and prompts     Grounded agent behavior

  Phase 5                 Evaluation and          T1--T12 + Langfuse
                          observability           evidence

  Phase 6                 Documentation and       GitHub + presentation
                          submission              
  -----------------------------------------------------------------------

## 9. Risks and Mitigations

  -----------------------------------------------------------------------
  Risk                    Impact                  Mitigation
  ----------------------- ----------------------- -----------------------
  API authentication      High                    OAuth2 validation,
  failure                                         secure credential
                                                  storage, controlled
                                                  testing

  Fabricated              High                    Grounding rules +
  calendar/email content                          tool-first
                                                  instructions +
                                                  evaluation

  Scheduling conflicts    High                    Availability check
                                                  before event creation

  Ambiguous user request  Medium                  Ask for clarification

  Excessive token usage   Medium                  Prompt optimization and
                                                  trace monitoring

  Sensitive data exposure High                    Least privilege,
                                                  minimization, secure
                                                  secrets

  Live API path not       High                    Connect, test, and
  validated                                       capture fresh traces
                                                  before production
                                                  claims
  -----------------------------------------------------------------------

## 10. Decision-Making

High-impact actions such as calendar creation or future email sending
should be subject to explicit user confirmation or human approval in a
production version.

## 11. Rollout Plan

1.  Validate live Google integrations.
2.  Run the complete baseline suite against the live path.
3.  Pilot with a small internal user group.
4.  Measure time saved, conflict reduction, latency, cost, and user
    satisfaction.
5.  Add human approval and improve prompts.
6.  Expand gradually toward the target user population.

## 12. Success Criteria

-   12/12 baseline tests pass.
-   Zero unsupported/hallucinated meeting or email content.
-   Full observability for validated runs.
-   Cost remains within the defined budget.
-   Production pilot demonstrates measurable time savings.
-   Security and privacy controls are reviewed before live deployment.
