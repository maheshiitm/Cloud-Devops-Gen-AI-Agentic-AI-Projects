# Mira — AI-Powered Project Intelligence Assistant

Capstone project for **Applied Agentic AI for PMs/TPMs**.

**Prepared by:** Mahesh Zade  
**Date:** September 2026

## 1. Executive Summary
Mira is an AI-powered project intelligence assistant designed for PMs/TPMs at Nexora. It automates three core activities using grounded project data:

1. Project plan generation
2. Risk assessment
3. Weekly status reporting

The implementation uses LangFlow, OpenAI (`gpt-4o-mini`) and Langfuse observability. The final workflow uses parallel specialist branches and a Prompt Template aggregation layer to produce one consolidated response.

## 2. Problem
PMs/TPMs spend significant manual effort creating plans, assessing risks and compiling weekly reports. The project brief identifies 3–4 hours of manual project-plan creation and 1–2 hours for weekly status compilation as key pain points.

## 3. Solution
Mira ingests the supplied project description, timeline, risk and task-board data and produces structured outputs grounded in those sources.

### Core agents
- **Project Planner Agent** — generates phases, activities and milestones from project description/timeline data.
- **Risk Assessor Agent** — produces categorized risks, impact and mitigations from the risk dataset.
- **Status Reporter Agent** — calculates task status counts and highlights blockers from the task board.
- **Prompt Template Aggregator** — consolidates specialist outputs into a single user-facing response.

### Guardrails
- Use only supplied project data.
- Do not invent milestones, tasks, risk ratings or progress.
- For insufficient/vague data, return an explicit `INSUFFICIENT DATA` response.
- Status counts must be calculated from the supplied task-board data.

## 4. Data Sources
The capstone brief identifies these inputs:
- `project_description.txt`
- `project_timeline.csv`
- `project_risks.csv`
- `sample_task_board.csv`
- `eval_mira_inputs.txt`

The original source document supplied for this package contains the capstone playbook, implementation notes, test history and written deliverables. The raw source datasets are **not recreated here**; upload the original dataset files if your course submission requires them.

## 5. Orchestration
### Final implemented pattern
**Parallel Pipeline + Prompt Template Aggregation**

The earlier design recommendation discussed Router/Dispatcher orchestration. During implementation, the workflow evolved to parallel specialist branches with centralized prompt aggregation. This avoided the practical limitation of connecting multiple specialist outputs directly into one downstream component and provided a clean consolidated response.

## 6. Observability
Langfuse is configured as the observability layer under the `Mira-Project-Prod` project. Traces capture inputs/outputs, OpenAI model calls, latency and token/cost information.

**Do not commit Langfuse secrets or OpenAI API keys.**

## 7. Baseline Evaluation
The capstone requires 12 baseline tests (T1–T12). The documented testing cycle initially exposed hallucination failures on vague inputs and a task-counting issue. The documented post-iteration result states that the Vague Input Rules and prompt changes resolved these edge cases and that the baseline criteria were subsequently passed.

See:
- `evaluation/Mira_Baseline_T1-T12_Results.csv`
- `evaluation/Mira_Baseline_T1-T12_Results.md`

**Evidence note:** the final PASS status is based on the completion narrative in the supplied playbook. For audit-grade evidence, keep/export the final Langfuse traces for T1–T12 and attach screenshots.

## 8. Cost and Production Metrics
The supplied project documentation estimates:
- ~2,000 input + ~1,500 output tokens per pipeline run
- ~$0.0005 per run
- ~10 runs/user/day
- ~$0.005/user/day
- ~$0.15/user/month under the stated assumptions

Production metrics:
- **Accuracy** — task counts/statuses match the source task board.
- **Trustworthiness** — hallucination rate / traceability of generated risks and milestones.
- **Usefulness** — hours saved versus the 3–4 hour manual planning baseline.

## 9. Program Rollout
The documented rollout plan targets 10 PMs/TPMs, with a 1-hour interactive workshop covering input formatting and human review of AI-generated artifacts.

## 10. Repository Structure
```text
Mira-AI-Project/
├── README.md
├── architecture/
│   └── Mira_Architecture_Diagram.png
├── docs/
│   ├── Q1_Ideation.md
│   ├── Q2_Build_Architecture.md
│   ├── Q3_Program_Charter.md
│   ├── Q4_Reflection.md
│   └── Completion_Audit.md
├── evaluation/
│   ├── Mira_Baseline_T1-T12_Results.csv
│   └── Mira_Baseline_T1-T12_Results.md
├── presentation/
│   └── Mira_Capstone_Presentation.pptx
├── workflow/
│   └── EXPORT_LANGFLOW_JSON_INSTRUCTIONS.md
├── screenshots/
│   └── README.md
└── source_data/
    └── README.md
```

## 11. Final Upload Requirement
Before final submission, export the **actual final LangFlow workflow JSON** from your working LangFlow instance and place it in `workflow/`. Do not substitute a manually recreated JSON.

Also add:
- workflow canvas screenshot
- Mira output screenshot
- Langfuse trace screenshots
- original input datasets, if required by your course/mentor

## 12. Security
Never upload `.env`, API keys, Langfuse secret keys, access tokens or other credentials.

