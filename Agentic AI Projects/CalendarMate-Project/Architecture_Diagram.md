# CalendarMate Architecture Diagram

## System Architecture Overview

```mermaid
graph TD
    User["👤 User Input<br/>(Chat/Schedule Trigger)"]
    
    User -->|Request| Orchestrator["🎯 Orchestrator Agent<br/>(Intent Classifier & Router)"]
    
    Orchestrator -->|Route: Briefing| BriefingAgent["📅 Briefing Agent<br/>Daily Summary Generator"]
    Orchestrator -->|Route: Schedule| SchedulerAgent["📆 Scheduler Agent<br/>Meeting Planner"]
    Orchestrator -->|Route: Email| EmailAgent["📧 Email Agent<br/>Inbox Manager"]
    Orchestrator -->|Route: Follow-up| FollowUpAgent["✅ Follow-Up Agent<br/>Post-Meeting Processor"]
    Orchestrator -->|Route: Conflict| ConflictAgent["⚠️ Conflict Resolver<br/>Conflict Detector"]
    
    BriefingAgent --> GoogleCalAPI1["🔗 Google Calendar API<br/>(Read Events)"]
    BriefingAgent --> GmailAPI1["🔗 Gmail API<br/>(Read Emails)"]
    
    SchedulerAgent --> GoogleCalAPI2["🔗 Google Calendar API<br/>(Check Availability<br/>Create Events)"]
    
    EmailAgent --> GmailAPI2["🔗 Gmail API<br/>(Read Inbox<br/>Search)"]
    
    FollowUpAgent --> GmailAPI3["🔗 Gmail API<br/>(Send Emails)"]
    FollowUpAgent --> GoogleCalAPI3["🔗 Google Calendar API<br/>(Read Event Details)"]
    
    ConflictAgent --> GoogleCalAPI4["🔗 Google Calendar API<br/>(Detect Conflicts)"]
    
    GoogleCalAPI1 --> CalendarData["📊 Calendar Data<br/>(Events, Attendees<br/>Availability)"]
    GoogleCalAPI2 --> CalendarData
    GoogleCalAPI3 --> CalendarData
    GoogleCalAPI4 --> CalendarData
    
    GmailAPI1 --> EmailData["📧 Email Data<br/>(Inbox, Attachments<br/>Metadata)"]
    GmailAPI2 --> EmailData
    GmailAPI3 --> EmailData
    
    BriefingAgent -->|Response| ResponseFormatter["📤 Response Formatter<br/>(Structured Output)"]
    SchedulerAgent -->|Response| ResponseFormatter
    EmailAgent -->|Response| ResponseFormatter
    FollowUpAgent -->|Response| ResponseFormatter
    ConflictAgent -->|Response| ResponseFormatter
    
    ResponseFormatter -->|Final Output| ChatOutput["💬 User Output<br/>(Chat Response<br/>Notification)"]
    
    ResponseFormatter -->|Trace Data| Langfuse["📊 Langfuse Observability<br/>(Traces, Tokens, Cost<br/>Quality Metrics)"]
    
    ChatOutput -->|Display| User
    
    style User fill:#e1f5ff
    style Orchestrator fill:#fff3e0
    style BriefingAgent fill:#f3e5f5
    style SchedulerAgent fill:#e8f5e9
    style EmailAgent fill:#fce4ec
    style FollowUpAgent fill:#e0f2f1
    style ConflictAgent fill:#ffe0b2
    style ResponseFormatter fill:#f1f8e9
    style ChatOutput fill:#c8e6c9
    style Langfuse fill:#ffccbc
```

---

## Agent Interaction Flow Diagram

```mermaid
sequenceDiagram
    participant User
    participant Orchestrator
    participant Briefing
    participant Scheduler
    participant Email
    participant FollowUp
    participant GoogleAPI as Google APIs
    participant Langfuse
    
    User->>Orchestrator: Send request
    
    Note over Orchestrator: Classify intent<br/>(Briefing/Schedule/Email/Follow-up)
    
    alt Briefing Request
        Orchestrator->>Briefing: Route to Briefing Agent
        Briefing->>GoogleAPI: Read calendar + emails
        GoogleAPI-->>Briefing: Return events & messages
        Briefing->>Briefing: Analyze & generate summary
        Briefing->>Langfuse: Log trace
        Briefing-->>Orchestrator: Return briefing
    else Scheduling Request
        Orchestrator->>Scheduler: Route to Scheduler Agent
        Scheduler->>GoogleAPI: Check availability
        GoogleAPI-->>Scheduler: Return slots
        Scheduler->>Scheduler: Propose times & create event
        Scheduler->>Langfuse: Log trace
        Scheduler-->>Orchestrator: Return confirmation
    else Email Request
        Orchestrator->>Email: Route to Email Agent
        Email->>GoogleAPI: Read inbox
        GoogleAPI-->>Email: Return emails
        Email->>Email: Summarize & prioritize
        Email->>Langfuse: Log trace
        Email-->>Orchestrator: Return summary
    else Follow-up Request
        Orchestrator->>FollowUp: Route to Follow-up Agent
        FollowUp->>GoogleAPI: Read meeting details
        GoogleAPI-->>FollowUp: Return event info
        FollowUp->>FollowUp: Generate summary & action items
        FollowUp->>GoogleAPI: Send follow-up emails
        FollowUp->>Langfuse: Log trace
        FollowUp-->>Orchestrator: Return confirmation
    end
    
    Orchestrator-->>User: Display response
```

---

## Data Flow Architecture

```mermaid
graph LR
    subgraph Input["Input Sources"]
        Chat["Chat Input"]
        Schedule["Schedule Trigger"]
        Webhook["Webhook Events"]
    end
    
    subgraph Processing["Processing Layer"]
        NLP["NLP Intent Classification"]
        Router["Request Router"]
        AgentPool["Agent Pool"]
    end
    
    subgraph Integration["Integration Layer"]
        CalAPI["Google Calendar API"]
        EmailAPI["Gmail API"]
        MeetAPI["Google Meet Integration"]
    end
    
    subgraph DataSources["Data Sources"]
        CalendarDB["Calendar Database"]
        InboxDB["Email Database"]
        EventDB["Event Metadata"]
    end
    
    subgraph Output["Output Layer"]
        Response["Formatted Response"]
        Email["Email Notification"]
        Calendar["Calendar Event"]
        Notification["Slack/Chat Alert"]
    end
    
    subgraph Observability["Observability & Analytics"]
        Traces["Langfuse Traces"]
        Metrics["Performance Metrics"]
        Feedback["User Feedback Loop"]
    end
    
    Input -->|Request| NLP
    NLP -->|Intent| Router
    Router -->|Dispatch| AgentPool
    
    AgentPool -->|Query| CalAPI
    AgentPool -->|Query| EmailAPI
    AgentPool -->|Create| MeetAPI
    
    CalAPI -->|Read/Write| CalendarDB
    EmailAPI -->|Read/Write| InboxDB
    CalAPI -->|Read| EventDB
    
    AgentPool -->|Process Results| Response
    
    Response -->|Display| Notification
    Response -->|Create| Calendar
    Response -->|Send| Email
    Response -->|Chat| Notification
    
    AgentPool -->|Send Data| Traces
    Traces -->|Analytics| Metrics
    Notification -->|Feedback| Feedback
    Feedback -->|Optimize| AgentPool
    
    style Input fill:#e3f2fd
    style Processing fill:#f3e5f5
    style Integration fill:#e8f5e9
    style DataSources fill:#fff3e0
    style Output fill:#fce4ec
    style Observability fill:#ffccbc
```

---

## Router Pattern Justification for CalendarMate

```mermaid
graph TD
    A["Different Request Types"] -->|Vary Significantly| B["Why Router Pattern?"]
    
    C1["Request: What's my day?"] -->|Different Handler| D["Router Pattern Benefits"]
    C2["Request: Schedule a meeting"] -->|Different Handler| D
    C3["Request: Summarize emails"] -->|Different Handler| D
    C4["Request: Generate follow-ups"] -->|Different Handler| D
    
    D -->|✅ Specialization| E["Each agent optimized<br/>for its domain"]
    D -->|✅ Efficiency| F["No unnecessary steps<br/>Only required agents process"]
    D -->|✅ Maintainability| G["Easy to update<br/>or add new agents"]
    D -->|✅ Scalability| H["Independent agent<br/>deployment & testing"]
    D -->|✅ User Experience| I["Faster responses<br/>Reduced latency"]
    
    E --> J["Router Pattern<br/>Selected ✓"]
    F --> J
    G --> J
    H --> J
    I --> J
    
    style A fill:#e3f2fd
    style B fill:#fff3e0
    style D fill:#f3e5f5
    style J fill:#c8e6c9
    style E fill:#e8f5e9
    style F fill:#e8f5e9
    style G fill:#e8f5e9
    style H fill:#e8f5e9
    style I fill:#e8f5e9
```

---

## Agent Responsibility Matrix

| Agent | Input Sources | Processing | Output | Tools |
|-------|---------------|-----------|--------|-------|
| **Orchestrator** | User request | Intent classification NLU | Routing decision | Claude LLM |
| **Briefing Agent** | Calendar events<br/>Recent emails | Summary generation<br/>Conflict detection<br/>Priority analysis | Daily briefing<br/>Conflicts list<br/>Focus plan | Calendar API<br/>Gmail API<br/>Claude LLM |
| **Scheduler Agent** | User request<br/>Calendar availability<br/>Attendee details | Availability checking<br/>Slot proposal<br/>Event creation<br/>Meet link generation | Confirmation message<br/>Calendar event<br/>Meet link | Calendar API<br/>Meet API<br/>Claude LLM |
| **Email Agent** | Gmail inbox<br/>Email search | Email summarization<br/>Priority grouping<br/>Action extraction | Email summary<br/>Priority list<br/>Action items | Gmail API<br/>Claude LLM |
| **Follow-Up Agent** | Meeting details<br/>Attendee info<br/>Discussion points | Action item extraction<br/>Summary generation<br/>Email composition | Follow-up email<br/>Action assignments | Gmail API<br/>Calendar API<br/>Claude LLM |
| **Conflict Resolver** | Calendar events<br/>Scheduling requests | Conflict detection<br/>Priority assessment<br/>Alternative slots | Conflict warning<br/>Suggestions<br/>Resolution options | Calendar API<br/>Claude LLM |

---

## Technology Stack Diagram

```mermaid
graph TB
    subgraph Application["Application Layer"]
        WebUI["Web/Chat Interface"]
        Mobile["Mobile App"]
    end
    
    subgraph Orchestration["Workflow Orchestration"]
        Langflow["Langflow<br/>(Agent Platform)"]
    end
    
    subgraph Agents["Agent Layer"]
        Claude["Claude 3.5 Sonnet<br/>(Reasoning Engine)"]
        Agents["Specialized Agents<br/>(5 Agents)"]
    end
    
    subgraph APIs["External APIs"]
        GoogleCal["Google Calendar API"]
        Gmail["Gmail API"]
        GoogleMeet["Google Meet API"]
    end
    
    subgraph Observability["Observability & Monitoring"]
        Langfuse["Langfuse<br/>(Traces, Cost, Metrics)"]
    end
    
    subgraph Database["Data Layer"]
        Cache["Response Cache"]
        Logs["Audit Logs"]
    end
    
    WebUI -->|Query| Langflow
    Mobile -->|Query| Langflow
    
    Langflow -->|Orchestrate| Agents
    Agents -->|Reasoning| Claude
    
    Agents -->|API Calls| GoogleCal
    Agents -->|API Calls| Gmail
    Agents -->|API Calls| GoogleMeet
    
    Langflow -->|Send Traces| Langfuse
    Agents -->|Send Metrics| Langfuse
    
    Agents -->|Cache Responses| Cache
    Langflow -->|Log Events| Logs
    
    style Application fill:#e3f2fd
    style Orchestration fill:#f3e5f5
    style Agents fill:#e8f5e9
    style APIs fill:#fff3e0
    style Observability fill:#ffccbc
    style Database fill:#fce4ec
```

---

## Deployment Architecture

```mermaid
graph TD
    subgraph Client["Client Layer"]
        Web["Web Browser"]
        Mobile["Mobile App"]
        Desktop["Desktop App"]
    end
    
    subgraph Load["Load Balancing"]
        LB["Load Balancer"]
    end
    
    subgraph Cloud["Cloud Infrastructure"]
        Instance1["Langflow Instance 1"]
        Instance2["Langflow Instance 2"]
        Instance3["Langflow Instance 3"]
    end
    
    subgraph Cache["Caching Layer"]
        Redis["Redis Cache<br/>(Response Cache)"]
    end
    
    subgraph External["External Services"]
        GoogleAPI["Google Cloud APIs<br/>(Calendar, Gmail, Meet)"]
        Claude["Claude API<br/>(Anthropic)"]
    end
    
    subgraph Monitoring["Monitoring & Observability"]
        Langfuse["Langfuse Dashboard"]
        Logs["Centralized Logs"]
    end
    
    Web -->|HTTPS| LB
    Mobile -->|HTTPS| LB
    Desktop -->|HTTPS| LB
    
    LB -->|Route| Instance1
    LB -->|Route| Instance2
    LB -->|Route| Instance3
    
    Instance1 -->|Cache Check| Redis
    Instance2 -->|Cache Check| Redis
    Instance3 -->|Cache Check| Redis
    
    Instance1 -->|API Call| GoogleAPI
    Instance1 -->|API Call| Claude
    Instance2 -->|API Call| GoogleAPI
    Instance2 -->|API Call| Claude
    Instance3 -->|API Call| GoogleAPI
    Instance3 -->|API Call| Claude
    
    Instance1 -->|Telemetry| Langfuse
    Instance2 -->|Telemetry| Langfuse
    Instance3 -->|Telemetry| Langfuse
    
    Instance1 -->|Logs| Logs
    Instance2 -->|Logs| Logs
    Instance3 -->|Logs| Logs
    
    style Client fill:#e3f2fd
    style Load fill:#fff3e0
    style Cloud fill:#f3e5f5
    style Cache fill:#e8f5e9
    style External fill:#fce4ec
    style Monitoring fill:#ffccbc
```

---

## Execution Flow: End-to-End Example

**Scenario:** User asks "Schedule a 30-minute meeting with sarah@company.com tomorrow at 2pm"

```mermaid
sequenceDiagram
    participant U as User
    participant LF as Langflow
    participant OA as Orchestrator Agent
    participant SA as Scheduler Agent
    participant CA as Google Calendar API
    participant GM as Google Meet API
    participant LFS as Langfuse
    
    U->>LF: Input: "Schedule a 30-minute...<br/>tomorrow at 2pm with sarah@..."
    
    LF->>OA: Route request
    Note over OA: Intent = "Schedule"<br/>Type = "Single attendee"
    
    OA->>SA: Dispatch to Scheduler Agent
    
    Note over SA: Extract details:<br/>Duration: 30 min<br/>Attendee: sarah@company.com<br/>Time: Tomorrow, 2pm
    
    SA->>CA: Query availability for<br/>sarah@company.com & user<br/>Tomorrow 2:00-2:30 PM
    
    CA-->>SA: ✅ Both available<br/>Slot confirmed
    
    SA->>CA: Create calendar event<br/>Title: "Meeting with Sarah"<br/>Time: Tomorrow 2:00-2:30 PM<br/>Attendees: User, sarah@company.com
    
    CA-->>SA: Event created<br/>Event ID: xyz123
    
    SA->>GM: Generate Google Meet link<br/>for Event ID: xyz123
    
    GM-->>SA: Meet link created<br/>https://meet.google.com/xyz
    
    SA->>CA: Update event with Meet link<br/>Description: Join meeting<br/>https://meet.google.com/xyz
    
    CA-->>SA: Event updated
    
    Note over SA: Generate response:<br/>✅ Meeting scheduled<br/>Tomorrow, 2:00-2:30 PM<br/>Attendee: sarah@company.com<br/>Meet Link: [URL]
    
    SA->>LFS: Send trace data<br/>Tokens: 1,200<br/>Latency: 1.4s<br/>Cost: $0.0045
    
    SA->>LF: Return formatted response
    
    LF->>U: Display confirmation<br/>✅ Meeting with Sarah scheduled<br/>Tomorrow at 2:00 PM<br/>Google Meet link included
    
    U-->>U: ✅ Task complete
```

---

## Summary

**Architecture Pattern:** Router / Dispatcher Pattern  
**Number of Agents:** 5 specialized agents + 1 orchestrator  
**API Integrations:** Google Calendar API, Gmail API, Google Meet API  
**LLM Engine:** Claude 3.5 Sonnet  
**Observability:** Langfuse (traces, cost analysis, quality metrics)  
**Status:** Production-ready with comprehensive monitoring  

---

*Created for CalendarMate Capstone - Mahesh P. Zade | 09 September 2026*
