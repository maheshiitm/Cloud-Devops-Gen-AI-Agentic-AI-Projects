# CalendarMate: AI-Powered Productivity Assistant
## Capstone Project - Agentic AI for PMs/TPMs

**Submitted by:** Mahesh P. Zade  
**Completion Date:** 09 September 2026  
**Acknowledgments:** Project completed with guidance from Gautam Muthukumar  
**Organization:** ServionIQ Solutions

---

## 📋 Project Overview

CalendarMate is an AI-powered multi-agent productivity assistant designed to reduce operational overhead for PMs, TPMs, and senior ICs at ServionIQ. The system addresses a critical pain point: professionals spending 2+ hours daily on meeting logistics, scheduling, and email triage instead of high-value work.

### The Problem
- **8-14 meetings** per day across engineering, product, design, and client teams
- **3-5 different calendars** requiring manual cross-referencing
- **30-45 minutes** every morning just figuring out the day's priorities
- **60+ emails** per day, many meeting-related
- **Frequent double-bookings** and missed follow-ups
- **No consolidated view** — constant context switching between calendar, email, Slack, and docs

### The Solution
CalendarMate uses a **Router-based orchestration pattern** with specialized agents to:
✅ Generate daily briefings with conflict detection  
✅ Intelligently schedule meetings with availability checking  
✅ Summarize and prioritize emails  
✅ Generate follow-up summaries with action items  
✅ Detect and resolve scheduling conflicts  

---

## 🏗️ Architecture

The system follows a **Router/Dispatcher Orchestration Pattern** where a central Orchestrator Agent classifies user intent and routes requests to specialist agents.

See `Architecture_Diagram.md` for detailed visual representation.

### Core Agents

| Agent | Responsibility |
|-------|-----------------|
| **Orchestrator Agent** | Classifies user intent and routes to appropriate specialist |
| **Briefing Agent** | Reads calendar + emails, generates daily summary with conflicts |
| **Scheduler Agent** | Checks availability, proposes slots, creates events with Google Meet |
| **Email Agent** | Reads inbox, groups by urgency/topic, separates action items |
| **Follow-Up Agent** | Generates post-meeting summaries and sends to attendees |

### Orchestration Pattern Selection: Router
**Why Router for CalendarMate:**
- User requests are highly varied ("What's my day look like?" vs "Schedule a meeting" vs "Summarize emails")
- Each request type has different requirements and logic
- Central dispatcher efficiently routes to the right specialist
- Allows for easy addition of new specialized agents
- Better resource utilization than sequential processing

---

## ✨ Core Capabilities (Implemented)

### 1. **Daily Briefing**
Consolidated summary of the day including:
- All meetings with times, attendees, and duration
- Scheduling conflicts detected and flagged
- Priority emails requiring response
- Suggested daily focus plan

### 2. **Smart Scheduling**
Natural language meeting requests with:
- Automatic availability checking across attendees
- Open time slot proposals
- Google Meet link generation
- Confirmation workflow for user approval

### 3. **Email Summarization**
Intelligent email processing:
- Groups emails by urgency (High/Medium/Low)
- Separates action-required vs FYI emails
- Extracts sender, subject, and key details
- Never fabricates email content

---

## 🚀 Extended Capabilities (Implemented)

### 4. **Meeting Follow-Up Generator**
- Automatic generation of follow-up summaries
- Action item extraction and assignment
- Email delivery to all meeting attendees

### 5. **Conflict Resolver**
- Real-time detection of scheduling conflicts
- Priority assessment
- Alternative time slot suggestions

---

## 📊 Testing & Evaluation

All 12 baseline test cases have been executed and documented:

| Test ID | Scenario | Status |
|---------|----------|--------|
| T1 | Daily briefing | ✅ Pass |
| T2 | Tomorrow's meetings | ✅ Pass |
| T3 | Single attendee scheduling | ✅ Pass |
| T4 | Ambiguous scheduling request | ✅ Pass |
| T5 | Multi-attendee scheduling | ✅ Pass |
| T6 | Edge case (weekend/unusual hours) | ✅ Pass |
| T7 | Email summarization | ✅ Pass |
| T8 | Action-required email filtering | ✅ Pass |
| T9 | Missing information handling | ✅ Pass |
| T10 | Weekly conflict detection | ✅ Pass |
| T11 | Conflict warning | ✅ Pass |
| T12 | Specific date briefing | ✅ Pass |

**Observability Integration:** Langfuse connected for tracing, token counting, and latency monitoring.

See `images/` folder for detailed screenshots of:
- Langflow workflow canvas
- Baseline test results
- Langfuse traces and cost analytics
- Dashboard overview

---

## 💰 Cost Analysis

**Cost Per User Per Day:**
```
Tokens per request (avg): ~1,500 tokens
Daily requests per PM/TPM: ~5-8
Model: Claude 3.5 Sonnet @ $3/1M input, $15/1M output
Estimated daily cost per user: $0.02-0.04
Monthly cost per user: $0.60-1.20
```

**Business Impact ROI:**
- 2 hours saved per PM/TPM per day
- 50 PMs/TPMs × 2 hours × ~$150/hour labor cost = **$15,000/day saved**
- Monthly savings: ~$300,000
- Payback period: < 1 day

---

## 🛠️ Tools & Technologies

| Category | Implementation |
|----------|-----------------|
| **Workflow Platform** | Langflow (Low-code agent orchestration) |
| **Calendar API** | Google Calendar API (availability checks, event creation) |
| **Email API** | Gmail API (inbox reading, summarization) |
| **LLM** | Claude 3.5 Sonnet (reasoning, summarization, NLU) |
| **Observability** | Langfuse (traces, cost tracking, quality metrics) |
| **Authentication** | OAuth2 (Google) for secure API access |

---

## 📁 Repository Structure

```
calendarmate-capstone/
├── README.md                              # This file
├── Architecture_Diagram.md                # Mermaid.js architecture visualization
├── CALENDARMATE_CAPSTONE-FINAL.json      # Langflow workflow export
├── SUBMISSION_CHECKLIST.md               # Submission validation checklist
└── images/
    ├── langflow-canvas.png               # Final wired agent workflow
    ├── baseline-tests-T1-T12.png         # Baseline test execution results
    ├── langfuse-trace-tokens.png         # Trace detail with cost/latency
    └── langfuse-dashboard.png            # Analytics dashboard overview
```

---

## 🔐 Security & Privacy Considerations

1. **OAuth2 Authentication:** Secure API access via Google OAuth2
2. **Data Minimization:** Only read necessary calendar and email data
3. **No Data Storage:** Real-time processing, no persistent data storage in workflow
4. **Prompt Injection Prevention:** Grounding rules prevent fabrication of meetings/emails
5. **Audit Trail:** Langfuse traces enable full observability and compliance logging

---

## 📈 Production Metrics

The following metrics are tracked via Langfuse:

1. **Agent Response Quality**
   - Baseline test pass rate: 100% (12/12)
   - False positive meeting fabrication: 0%
   - Conflict detection accuracy: 100%

2. **System Performance**
   - Average latency per request: 1.2-1.8 seconds
   - Token utilization: ~1,500 tokens/request
   - Cost per request: $0.004-0.008

3. **User Adoption**
   - Expected initial adoption: 10 PMs/TPMs (pilot)
   - Rollout to full 50 PMs/TPMs: Week 4-6
   - Target usage: 5-8 requests per user per day

---

## 🎯 Next Steps & Improvement Plan (2-Week Sprint)

### Week 1: Pilot Launch
- [ ] Deploy to 10 PM/TPM users
- [ ] Gather real-world usage feedback
- [ ] Monitor Langfuse traces for edge cases
- [ ] Fine-tune system prompts based on real calendar data

### Week 2: Optimization
- [ ] Analyze user feedback and error patterns
- [ ] Fine-tune Claude model on domain-specific terminology
- [ ] Implement human-in-the-loop approvals for sensitive scheduling
- [ ] Scale to 30 additional PMs/TPMs based on pilot results

### Planned Enhancements
- [ ] Attendee research with email history integration
- [ ] Weekly digest generation with focus time analysis
- [ ] Slack integration for seamless notifications
- [ ] Calendar conflict auto-resolution using AI recommendations
- [ ] Custom fine-tuning model trained on ServionIQ meeting patterns

---

## 📚 Curriculum Concepts Applied

| Concept | Application |
|---------|-------------|
| **Multi-Agent System Design** | 5 specialized agents with clear responsibilities and defined interfaces |
| **Orchestration Patterns** | Router pattern for request classification and agent routing |
| **Prompt Engineering** | Grounding rules to prevent fabrication; structured output formats |
| **Tool Integration** | Google Calendar API and Gmail API via HTTP nodes |
| **Evaluation & Observability** | Langfuse integration with traces, token counting, latency monitoring |

---

## 🤝 Program Charter Highlights

**Vision:** Empower ServionIQ's PMs/TPMs to reclaim 2+ hours daily by automating meeting logistics and email triage.

**Success Criteria:**
- Reduce meeting logistics time from 2 hours to 30 minutes per day
- 100% accuracy in conflict detection (zero missed double-bookings)
- 95%+ user satisfaction in pilot phase
- < 2 seconds latency on all agent responses

**Timeline:**
- Week 1-2: Development & testing (COMPLETED)
- Week 3-4: Pilot deployment to 10 users
- Week 5-6: Feedback & optimization
- Week 7-8: Scale to 50+ PMs/TPMs

**Risk Mitigation:**
- API rate limits: Implement caching and batch processing
- Data privacy: Ensure OAuth2 compliance and audit logging
- User adoption: Comprehensive onboarding and dedicated support

---

## 📝 Submission Details

**Submission Date:** 09 September 2026  
**Project Lead:** Mahesh P. Zade  
**Supporting Contributor:** Gautam Muthukumar  
**Institution:** ServionIQ Solutions - Applied Agentic AI Capstone  

---

## 📞 Support & Questions

For questions about this implementation or architecture, please refer to:
- Architecture diagram: `Architecture_Diagram.md`
- Workflow export: `CALENDARMATE_CAPSTONE-FINAL.json`
- Test results: `images/baseline-tests-T1-T12.png`

---

**Status:** ✅ Ready for Submission

---

*CalendarMate © 2026 | Mahesh P. Zade | Capstone Project*
