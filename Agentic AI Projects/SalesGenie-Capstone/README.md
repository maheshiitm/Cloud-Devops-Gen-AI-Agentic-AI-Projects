# SalesGenie: AI-Powered Sales Assistant

**Capstone Project — Applied Agentic AI for PMs/TPMs**

**Author:** Mahesh Zade  
**Special Thanks:** Gautam Muthukumar for completing the Project and the Interview Kickstart team.

## 1. Project Overview

SalesGenie is an AI-powered sales assistant for Oak & Ember Interiors. The capstone problem statement describes a sales process where representatives spend 2–3 hours per day manually reading inbound inquiries, manual Excel entry introduces errors, product matching is time-consuming, lead scoring is inconsistent, CRM visibility is delayed, and weekly insights are compiled manually.

The target solution is a multi-agent workflow that:
1. Ingests and extracts customer inquiry fields.
2. Qualifies leads as Hot / Warm / Cold.
3. Recommends 1–3 catalog-grounded products.
4. Drafts a personalized response.
5. Supports weekly sales insights as a separate capability.

## 2. Current Implemented Workflow

The supplied LangFlow JSON contains **11 nodes / 10 edges**:
- Chat Input
- Email Ingestion Agent prompt
- OpenAI LLM
- Lead Qualifier Agent prompt
- OpenAI LLM
- File Ingestion Component
- Product Recommender Agent prompt
- OpenAI LLM
- Response Drafter prompt
- OpenAI LLM
- Chat Output

The workflow follows a **Sequential Pipeline**:

`Inbound inquiry → Email Ingestion → Lead Qualification → Product Recommendation → Response Drafting → Chat Output`

The capstone guidance specifically recommends a sequential pipeline for SalesGenie because the standard inquiry path follows the same ordered stages.

## 3. Tools

| Area | Choice |
|---|---|
| Workflow platform | LangFlow |
| LLM | OpenAI `gpt-4o-mini` |
| Data grounding | `product_catalog.csv` via File component |
| Observability | Langfuse, as described in the supplied project documentation |
| Output | Customer-ready response in Chat Output |
| Workflow export | `workflow/Sales_Genie_Project.json` |

## 4. Agent Responsibilities

### Email Ingestion Agent
Extracts:
- name
- email
- product interest
- budget
- urgency

The supplied prompt instructs the agent to use `UNKNOWN` when a field is not explicitly stated.

### Lead Qualifier Agent
Adds `lead_tier` and classifies the lead as Hot / Warm / Cold. The prompt also states that spam or non-lead messages should not be classified as leads.

### Product Recommender Agent
Receives qualified lead data plus the actual product catalog and recommends matching products with rationale.

### Response Drafter
Turns the recommendation output into a professional customer response.

## 5. Data Grounding

The supplied catalog contains 20 furniture/accessory products with product ID, product name, category, price, description, availability, material and dimensions.

Examples:
- Walnut Executive Desk — **Out of Stock**
- Adjustable Standing Desk Pro — **$749, In Stock**
- Ergonomic Pro Chair — **$449, In Stock**
- Conference Table 12-Person — **$2,499, In Stock**
- Desk Organizer Set — **$39, In Stock**

The catalog is the source of truth for product recommendations, pricing and availability.

## 6. Evaluation

The capstone requires all 11 baseline inputs to be tested and documented.

The supplied baseline workbook was reviewed against the supplied catalog. The observed outputs contain significant grounding and routing failures, including invented product names, unsupported features, incorrect stock reporting for T10, and failure to produce the required weekly summary for T11.

**Therefore this repository deliberately does not claim 11/11 passing results.** The file `evaluation/Baseline_Test_Results_Reviewed.xlsx` records the observed gaps. Before final academic submission, rerun T1–T11 on the live workflow and replace the review with verified execution evidence.

## 7. Important Implementation Gaps to Resolve Before Final Submission

1. **Catalog grounding must be enforced:** recommendations must only use products present in `resources/product_catalog.csv`.
2. **Non-lead routing:** product questions and spam should not be forced through Hot/Warm/Cold qualification.
3. **Out-of-stock handling:** T10 must return the catalog's actual stock status.
4. **Weekly summary:** T11 needs a dedicated weekly aggregation path based on processed lead data.
5. **Response Drafter prompt:** the supplied exported workflow contains a hard-coded customer name (“Sarah”); this should be changed to use the extracted customer name dynamically.
6. **Baseline evidence:** rerun all 11 tests and capture the outputs and Langfuse traces.

## 8. Repository Structure

```text
SalesGenie-Capstone/
├── README.md
├── workflow/
│   └── Sales_Genie_Project.json
├── docs/
│   ├── SalesGenie_Project_Report_Q1-Q4.docx
│   └── SalesGenie_Presentation_25_Slides.pptx
├── architecture/
│   └── SalesGenie_Architecture.png
├── evaluation/
│   ├── Baseline_Test_Results_Reviewed.xlsx
│   ├── Baseline_Review.md
│   └── Baseline_11_Test_Cases_and_Prompts_Source.xlsx
├── resources/
│   ├── sample_inquiry_emails.txt
│   ├── product_catalog.csv
│   ├── crm_export_sample.csv
│   └── eval_salesgenie_inputs.txt
├── evidence/
│   ├── SalesGenie_Workflow_Canvas.png
│   └── GitHub_Current_State.png
└── demo/
    └── SalesGenie_Demo_5min.mp4
```

## 9. Submission Checklist

- [x] README
- [x] Exported LangFlow JSON
- [x] Architecture diagram
- [x] 25-slide presentation
- [x] Workflow canvas screenshot
- [x] GitHub screenshot
- [x] 5-minute demo video
- [x] Baseline test source and reviewed results
- [x] Q1–Q4 project report
- [ ] Final verified T1–T11 run against the live workflow
- [ ] Final Langfuse trace screenshots for the verified run

## 10. Credits

**Project:** SalesGenie — AI-Powered Sales Assistant  
**Author:** Mahesh Zade  
**Special Thanks:** Gautam Muthukumar for completing the Project and the Interview Kickstart team.
