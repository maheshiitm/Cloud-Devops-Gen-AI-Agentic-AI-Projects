# PRD Genie — Q1–Q4 Assignment Answers

## Q1 — Ideation
1. Manual requirement capture → Requirement Extractor.
2. Inconsistent PRD formats → fixed PRD template/generation agent.
3. Manual Epic/User Story creation → Story Breakdown agent.
4. Lost/ambiguous requirements → Gap Analyzer and source evidence.
**Primary risk:** hallucinated requirements.

## Q2 — Program Charter
**Vision:** Reduce repetitive PM/TPM documentation work while improving consistency and traceability.

**Objectives:** Improve extraction completeness, reduce hallucination, standardize PRD structure and accelerate story creation.

**In scope:** transcript/notes input, requirement extraction, PRD generation, story breakdown, Gap Analysis, Langfuse and baseline evaluation.

**Out of scope:** autonomous product decisions, external system writes, fine-tuning and RAG unless added later.

## Q3 — Build PRD Genie
LangFlow implements the Sequential Pipeline. OpenAI nodes perform extraction and generation. Langfuse provides observability. Gap Analysis is the selected extended capability.

## Q4 — Reflection
Baseline traces showed that fluent output can still be unsupported. The key learning was that every agent needs an explicit insufficient-input policy. The revised prompts therefore require source evidence, prohibit role inference, preserve contradictions and force UNKNOWN/TBD handling.
