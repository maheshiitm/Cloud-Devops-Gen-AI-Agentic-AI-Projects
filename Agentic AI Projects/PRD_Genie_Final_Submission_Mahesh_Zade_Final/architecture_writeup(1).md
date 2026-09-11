# PRD Genie — Final Architecture & Evaluation Writeup

**Prepared by:** Mahesh Zade  
**Special thanks:** Gautam Muthukumar for helping with the project, and the entire Interview Kickstart team for helping achieve the goal.

## 1. Problem Summary
PRD Genie helps PMs/TPMs translate meeting discussions, transcripts and notes into structured product documentation. The Playbook identifies the core PRD Genie wastes as rewriting transcripts into structured documents, inconsistent PRD formats and lost requirements, with hallucinated requirements as the key AI risk. PRD Genie addresses this through a grounded sequential pipeline that extracts source facts, generates a structured PRD, breaks explicit functional requirements into stories, and surfaces gaps.

## 2. Architecture and Orchestration
The selected orchestration pattern is a **Sequential Pipeline**, matching the Playbook's PRD Genie recommendation: extract → PRD → stories. The final flow is:

**Chat Input → Requirement Extractor → PRD Generator → Story Breakdown → Final Output Assembler**

The **Gap Analyzer** receives the extractor output in parallel with the downstream PRD/story path and contributes stakeholder clarification questions to the final assembled response.

## 3. Tool Selection
| Category | Final Choice | Rationale |
|---|---|---|
| Workflow Platform | LangFlow | Visual agent builder suited to multi-agent pipelines and custom prompts; explicitly recommended for PRD Genie in the Playbook. |
| LLM | OpenAI GPT-4o-mini | Cost-conscious model configured in the flow for extraction and generation. |
| Observability | Langfuse | Provides trace-level visibility into inputs/outputs, latency, tokens and cost. |
| Input / Output | LangFlow Chat Input / Chat Output | Simple text-based transcript/notes entry and final specification display. |

## 4. Agent Responsibilities
**Requirement Extractor:** separates stated requirements from NFRs, stakeholders/roles, deadlines, ambiguity, contradictions, dependencies/risks and source evidence.

**PRD Generator:** produces the required 11-section PRD while preserving source facts and refusing to invent personas, goals, acceptance criteria, benefits, or unsupported scope.

**Story Breakdown:** creates Epic → Feature → User Story only from explicit functional requirements. NFRs such as performance, response time, capacity and concurrency are excluded from story generation.

**Gap Analyzer:** asks targeted clarification questions for ambiguity, UNKNOWN/TBD items, contradictions, insufficient information and decision-requiring dependencies.

**Final Output Assembler:** combines PRD, stories and gap analysis into the final product specification.

## 5. Prompt Engineering / Iteration
The evaluation loop was **Evaluate → Find failure → Fix prompt → Re-evaluate → Confirm improvement**. The revised prompts added explicit insufficient-input rules, strict source grounding, generic-actor versus formal-persona handling, NFR exclusion, capacity/scalability exclusion, dependency handling, contradiction preservation and story traceability.

## 6. Baseline Evaluation — Final Result
**12/12 baseline tests PASS (100%).**

| Area | Result |
|---|---|
| Detailed functional requirements | PASS |
| Ambiguous competitor/reference input | PASS |
| Contradiction / NFR handling | PASS |
| Exact acceptance constraints | PASS |
| Insufficient information | PASS |
| Stakeholder preference vs requirement | PASS |
| Technical NFR classification | PASS |
| Explicit persona mapping | PASS |
| Empty-source handling | PASS |
| Dependency + UNKNOWN ETA | PASS |
| T1 → grounded PRD (T11) | PASS |
| T11 → traceable stories (T12) | PASS |

### Key validation examples
- **T1:** date/category/status filtering is functional; `<2 seconds` remains an NFR; Sarah and Q3 are preserved.
- **T7:** `10,000 concurrent users` and `<200ms p95` remain NFRs; Salesforce REST API v52 produces the functional story.
- **T8:** Admins, End users and Auditors are preserved as explicit personas and mapped to their own stories.
- **T10:** SSO dependency on Team Alpha is preserved and the only clarification question asks for the expected ETA.
- **T12:** exactly three filtering stories are generated; no performance story is created.

## 7. Langfuse Observability
The supplied final-run screenshots show Langfuse tracing with Chat Input, Prompt Template, OpenAI generations and Chat Output, along with latency/cost fields. One displayed trace shows approximately **7.26 seconds** total latency and **$0.001684** total cost for that observed run. This is a sample observed trace, not a universal per-run cost guarantee; production cost should be calculated from representative trace samples.

## 8. Production Metrics
1. **Extraction completeness** — percentage of stated requirements correctly captured.
2. **Hallucination rate** — percentage of generated PRD items not traceable to source.
3. **Format compliance** — percentage of PRDs following the required structure.

Operational metrics can additionally include latency, token usage and cost per pipeline run.

## 9. Cost Analysis
Observed Langfuse trace evidence should be used for actual cost reporting. The business formula is:

**Monthly cost/user = cost per run × runs per user per day × 30**

The ROI deck intentionally separates illustrative scenarios from measured financial outcomes.

## 10. Submission Alignment
The final package contains the workflow JSON, baseline results, architecture diagram, architecture writeup, README, Q1–Q4 answers, reflection, prompts, screenshots, 25-slide presentation, ROI/business-impact presentation, GitHub guide and compressed demo video. The Playbook's Step 7 checklist specifically calls for workflow JSON, architecture diagram, baseline results, workflow/system/observability screenshots, architecture writeup, assignment answers, slide deck and public GitHub link.
