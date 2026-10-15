# E-Commerce AI Customer Support Copilot
**Author:** Mahesh Zade
**Role:** AI Technical Program Manager (TPM)
**Project:** Week 4 Final Assignment – Agentic AI System Design

---

## PART 1: PRODUCT THINKING 

### 1. Problem Framing
**Clarifying the Problem:**
E-commerce support currently relies on human agents manually pulling data from fragmented sources (order history, policies, past chats), resulting in slow, inconsistent resolutions and high costs. 
*   *Primary User:* The human customer support agent (Copilot model), with secondary impact on the end consumer.
*   *Current Pain:* High Average Handle Time (AHT) and inconsistent policy application.
*   *Success Definition:* A reduction in resolution time and cost-per-contact while maintaining or increasing CSAT for high-value customers.

### 2. Assumptions & Alignment
*   **Assumptions:** The e-commerce platform has accessible APIs for order management, and policy documents are centralized but lengthy. 
*   **Goal Alignment:** The business is trying to optimize operational efficiency (reducing cost per ticket) without sacrificing the white-glove experience expected by high-value buyers.

### 3. Success Metrics
*   **North Star KPI:** **Average Handle Time (AHT) per resolved ticket.** This ties directly to operational cost savings and user wait times.
*   **Supporting KPIs:** 
    *   *Quality:* First Contact Resolution (FCR) rate.
    *   *Engagement/Adoption:* Percentage of support tickets where the agent uses the Copilot's drafted response.
*   **Out of Scope:** We are *not* optimizing for full customer deflection (Level 0 chatbots). This is an agent-assist tool.

### 4. Customer Segmentation
We segment by behavior to maximize impact on the North Star.
*   *Segments:* High-frequency/High-value buyers vs. Casual/Guest buyers.
*   *Selected Segment:* **High-frequency, high-value customers.** They drive a disproportionate share of support volume and have complex, multi-order histories that currently take human agents the longest to parse.

### 5. Problem Selection
*Problems for the High-Value Segment:*
1.  Delayed responses due to agents manually searching through past interactions.
2.  Inconsistent application of VIP return policies.
3.  Lack of proactive context (e.g., agent doesn't realize the customer had a delayed order last week).
*   **Selected Problem:** Agents manually pulling fragmented data (order status + policy + chat history) to formulate a compliant response. This is highly solvable with AI retrieval.

### 6. Solutioning
**The AI Support Copilot Dashboard:**
A side-panel UI in the agent's CRM (e.g., Zendesk/Salesforce) that listens to the live chat. 
*   **Where AI comes in:** The system automatically extracts customer intent from the incoming message, queries the backend database for order context, retrieves the relevant return/shipping policy via RAG, and generates a pre-drafted, policy-compliant response for the human agent to review, edit, and send.

---

## PART 2: AI SYSTEM DESIGN 

### 7. AI Approach Framing
This requires a **probabilistic, model-based** approach combined with **deterministic tool execution**. Generating empathetic, context-aware responses is probabilistic (LLM), but fetching the exact order status must be deterministic (API).

### 8. Model Choice
*   **Choice:** Hybrid system utilizing an LLM (e.g., GPT-4o-mini or Claude 3 Haiku) for intent routing and generation, alongside traditional deterministic APIs for data fetching.
*   **Why:** We prioritize low latency (sub-2 second response generation for live chat) and high interpretability.

### 9. Pre-Training Considerations
*   **Base Model:** We will use a generalized, commercial foundation model (like GPT-4o) rather than training a model from scratch. 
*   **Why:** Generalization is sufficient for natural language understanding; specialization will be handled via our retrieval architecture.

### 10. Post-Training / Adaptation
*   **Approach:** **RAG (Retrieval Augmented Generation)** combined with strict prompt engineering. 
*   **Why not fine-tuning?** E-commerce policies, shipping delays, and inventory change dynamically. Fine-tuning bakes stale facts into model weights. RAG allows us to swap out dynamic knowledge instantly without retraining.

### 11. RAG Design
We need external knowledge because the hallucination risk for return policies is high.
*   **Data Sources:** Enterprise Confluence/Notion (Policies), CRM (Customer History).
*   **Chunking Strategy:** Semantic, clause-level chunking for policy documents so exceptions (e.g., "30 days, *except* for electronics") are not split.
*   **Retrieval:** Hybrid search (Dense embeddings for policy matching + Keyword/SQL search for exact Order IDs).

### 12. Data Strategy & Golden Dataset
*   **Golden Dataset Definition:** 1,000 highly curated, expert-reviewed support interactions representing our top 20 intents (e.g., "Where is my order", "Refund request"). 
*   **"Good Output":** A response that accurately cites the policy, includes the correct order ID, maintains brand tone, and proposes the next best action.

### 13. Precision vs. Recall Tradeoff
*   **Stance:** **Precision focus**.
*   **Why:** In high-stakes support (e.g., promising a $500 refund), we must avoid wrong answers at all costs. We prefer the model abstains (fails to generate a draft) rather than confidently hallucinating a fake policy exception.

### 14. Evaluation & Testing
*   **Offline Testing:** 
    *   *Accuracy & Groundedness:* Using an LLM-as-a-judge against our Golden Dataset.
*   **Online Testing:** A/B testing Copilot-enabled agents vs. standard agents. Measuring AHT and Task completion rate.
*   **Human Evaluation:** Rubric grading based on Correctness, Relevance, and Tone.

### 15. Human-in-the-Loop (RLHF)
*   The human agent is the ultimate safety layer. The Copilot only *drafts* responses; the human clicks "Approve" or edits the text.
*   **Feedback Capture:** We capture explicit telemetry. If an agent heavily edits the drafted text before sending, the system logs the delta (difference) and flags it for prompt-tuning review.

### 16. System Architecture
1.  **Input:** Customer message arrives via web hook.
2.  **Intent Router (LLM):** Classifies issue (e.g., "Refund").
3.  **Retrieval Layer (RAG):** Fetches Order API (deterministic) + Policy Vector DB (semantic).
4.  **Generation (LLM):** Synthesizes context into a draft.
5.  **Output:** Displayed in Agent UI.
6.  **Feedback Loop:** Agent edits/approves -> logged to evaluation database.

### 17. Operationalization
*   **Latency:** Streaming responses to the UI so the agent sees text generating instantly (real-time vs batch).
*   **Cost:** Utilize smaller models (e.g., GPT-4o-mini) for intent routing to save inference costs, reserving large models only for complex policy synthesis.
*   **Monitoring:** Track embedding drift and token usage spikes.

### 18. Safety & Guardrails
*   **Hallucination Mitigation:** Output is cross-referenced with retrieved chunks. If the generated text contains a dollar amount not found in the source chunk, it is blocked.
*   **Toxicity:** Input/Output filters to prevent agents from accidentally sending frustrated remarks.

### 19. Go / No-Go Decision Framework
*   **Launch IF:** AHT improves by >15% without a drop in CSAT, and fatal error rate (hallucinated policies) on the golden set is <1%.
*   **Do NOT Launch IF:** Hallucination risk on refund policies remains high, or if API latency adds more wait time than the manual search process.

### 20. Trade-offs
*   **Automation vs. Control:** We traded full customer-facing automation (chatbots) for human-in-the-loop control to guarantee policy compliance for high-value users.
*   **Cost vs. Quality:** We incur LLM inference costs per ticket, offset by the reduction in human labor time (AHT).
