---
marp: true
theme: default
paginate: true
size: 16:9
---

# E-Commerce AI Customer Support Copilot
**Author:** Mahesh Zade  
**Role:** AI Technical Program Manager (TPM)  
**Project:** Week 4 Final Assignment – Agentic System Design  

---

## 1. Problem Framing & Success Metrics
* **The Problem:** E-commerce support relies on human agents manually pulling info from fragmented sources, causing slow resolutions and high costs.
* **Target Segment:** High-frequency, high-value VIP customers.
* **North Star KPI:** Average Handle Time (AHT) per resolved ticket.
* **Supporting KPIs:** First Contact Resolution (FCR), Copilot Adoption Rate.
* **Out of Scope:** Level 0 customer-facing deflection. This is strictly Agent-Assist.

---

## 2. Solution: The AI Copilot
**What it does:** An intelligent side-panel inside the agent CRM.  
**Where AI comes in:** 
1. Extracts customer intent from live chat.
2. Queries deterministic databases for Order IDs.
3. Retrieves return/shipping policies via RAG.
4. Generates a policy-compliant response draft for the human to review.

---

## 3. AI System Design: RAG vs. Fine-Tuning
* **Approach:** Probabilistic generation (LLMs) + Deterministic execution (APIs).
* **Adaptation:** We use **RAG (Retrieval-Augmented Generation)**, NOT fine-tuning.
* **Why RAG?** E-commerce policies and inventory change dynamically. RAG prevents the model from memorizing stale facts and allows instant knowledge updates without retraining.
* **Precision vs. Recall:** Strict **Precision focus**. We prefer the model abstains rather than hallucinating an invalid refund policy.

---

## 4. Evaluation & Human-in-the-Loop
* **Golden Dataset:** 1,000 highly curated, expert-reviewed interactions covering the top 20 intents.
* **Offline Eval:** LLM-as-a-judge scoring Groundedness against the Golden Set.
* **Human-in-the-Loop (HITL):** Copilot drafts only; humans approve/edit. 
* **Feedback Loop:** Heavy agent edits are captured via telemetry as negative signals for prompt-tuning.

---

## 5. Launch Governance & Trade-offs
**Go / No-Go Framework:**
* **Launch IF:** AHT improves >15%, CSAT remains stable, and hallucination rate <1%.
* **Do NOT Launch IF:** API latency exceeds manual search time.

**Trade-offs:**
* *Automation vs. Control:* Traded fully autonomous bots for Human-in-the-Loop safety to protect high-value buyers.
* *Cost vs. Quality:* Paid LLM inference costs per ticket to drastically reduce human labor time (AHT).
