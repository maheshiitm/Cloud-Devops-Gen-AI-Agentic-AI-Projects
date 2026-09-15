# Q4 — Reflection and Next Steps

## 1. Trace Findings
Langfuse provided visibility into execution paths, latency and token consumption. Initial traces showed that detailed inputs were handled well, while vague inputs caused hallucinated plans/risk matrices.

## 2. Improvement
The system was strengthened with centralized prompt aggregation and strict Vague Input Rules. Planner, Risk Assessor and Status Reporter prompts explicitly require grounding and refusal/`INSUFFICIENT DATA` behavior when required information is missing.

## 3. Fine-Tuning / Future Iteration
The current design uses zero-shot prompting. A future iteration can create a JSONL dataset of corrected vague-input examples and evaluate fine-tuning of `gpt-4o-mini`. For larger multi-turn workloads, a dedicated orchestration/state layer or message broker could improve fault tolerance.

## 4. Privacy
Raw project data should be sanitized for client PII before ingestion. External LLM access should use an approved enterprise gateway/control plane and appropriate data-retention settings.

## 5. Rollout to 10 PMs/TPMs
The documented plan uses a containerized deployment, Git version control and a 1-hour workshop covering CSV formatting and human review of generated artifacts before client delivery.
