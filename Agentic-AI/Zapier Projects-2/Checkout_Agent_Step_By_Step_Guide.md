# Checkout Incident Detection Agent — Complete Assignment Guide

---

## PART 1 — GOOGLE SHEETS SETUP

### Step 1: Import the Spreadsheet into Google Sheets

1. Download the `.xlsx` file provided (Checkout_Incident_Detection_Agent.xlsx).
2. Go to [sheets.google.com](https://sheets.google.com) → click **"+"** (New spreadsheet).
3. Go to **File → Import → Upload** → select the `.xlsx` file.
4. Choose **"Replace spreadsheet"** and click **Import data**.
5. You now have all 4 sheets: `Cart_Events`, `Baseline_Metrics`, `State`, `Agent_Commands`.

---

### Sheet 1 — Cart_Events (Input)

| timestamp | checkout_step | cart_value | device |
|---|---|---|---|
| 2026-01-28 13:30:00 | PAYMENT | 4599 | MOBILE |
| 2026-01-28 13:45:00 | PAYMENT | 4599 | MOBILE |
| 2026-01-28 14:00:00 | PAYMENT | 5200 | MOBILE |
| 2026-01-28 14:10:00 | ADDRESS | 30 | MOBILE |
| 2026-01-28 14:15:00 | SHIPPING | 1199 | DESKTOP |
| ... (15 rows total) | | | |

**Purpose:** Every checkout failure event goes here. New rows = new events for the agent to process.

---

### Sheet 2 — Baseline_Metrics (Context)

| checkout_step | baseline_rate |
|---|---|
| PAYMENT | 9.8 |
| ADDRESS | 3.2 |
| SHIPPING | 5.6 |

**Purpose:** Normal failure rates per step. The agent compares live failure rates against these to detect anomalies.

---

### Sheet 3 — State (Memory)

| key | value |
|---|---|
| last_processed_timestamp | 2026-01-28 13:15:00 |

**Purpose:** The agent reads this at the start of every run to know which events are "new". It updates this value at the end of each run.

---

### Sheet 4 — Agent_Commands (Output)

Columns: `command_id`, `action`, `severity`, `reason`, `checkout_step`, `cart_value`, `device`, `baseline_rate`, `timestamp`

**Purpose:** The agent writes exactly one row here per decision (ALERT or LOG). This is also the webhook payload source.

---

## PART 2 — ZAPIER AGENT SETUP

### Step 2: Create a New Zapier Agent

1. Go to [zapier.com](https://zapier.com) → Click **"Agents"** in the left sidebar.
2. Click **"+ New Agent"**.
3. Name it: `Checkout Incident Detection Agent`.

---

### Step 3: Write the Agent Instructions (System Prompt)

Paste this exactly as the agent's instructions:

```
You are an E-commerce Operations Agent that monitors checkout failures.

TOOLS AVAILABLE:
- Google Sheets (read/write)
- Webhook (POST)

YOUR TASK ON EVERY RUN:

STEP 1 — READ STATE
Read the value of `last_processed_timestamp` from the "State" sheet (cell B2).

STEP 2 — FETCH NEW EVENTS
Read all rows from the "Cart_Events" sheet where the `timestamp` column is NEWER than the last_processed_timestamp you just read. If no new rows exist, write one LOG row to Agent_Commands with reason "No new cart events to process" and stop.

STEP 3 — EVALUATE EACH NEW EVENT
For each new event, apply these rules to determine severity:

HIGH severity if ANY of these are true:
  a. checkout_step = "PAYMENT" (critical revenue step)
  b. cart_value > 1000 (significantly high value)
  c. failure_rate_for_this_step > baseline_rate (look up from Baseline_Metrics sheet)
  d. 2 or more events in this batch have device = "MOBILE" (potential app bug)

LOW severity: if none of the HIGH conditions are met.

Action:
  - ALERT → if severity is HIGH
  - LOG   → if severity is LOW

STEP 4 — WRITE TO AGENT_COMMANDS SHEET
For each decision, append exactly ONE row to the "Agent_Commands" sheet with:
  - command_id: CMD_[YYYYMMDD]_[3-digit-sequence]
  - action: ALERT or LOG
  - severity: HIGH or LOW
  - reason: human-readable explanation of why
  - checkout_step: from the event
  - cart_value: from the event
  - device: from the event
  - baseline_rate: looked up from Baseline_Metrics for this step
  - timestamp: the event's timestamp

STEP 5 — FIRE WEBHOOK
After writing the row, POST to the configured webhook URL with a JSON body containing all 9 fields listed above.

STEP 6 — UPDATE STATE
After processing all events, update cell B2 in the "State" sheet with the timestamp of the LATEST event you just processed.

RULES:
- Never process the same event twice (state management prevents this).
- Always write exactly one row per decision.
- Always fire the webhook for every decision.
```

---

### Step 4: Connect Google Sheets to Zapier

1. In your Agent's **Tools** section, click **"+ Add Tool"** → search **Google Sheets**.
2. Click **Connect** → sign in with the Google account that owns your spreadsheet.
3. Grant permissions and select your spreadsheet.
4. Add these actions:
   - **Read Spreadsheet Rows** (for Cart_Events, Baseline_Metrics, State)
   - **Update Spreadsheet Row** (for State sheet)
   - **Create Spreadsheet Row** (for Agent_Commands)

---

### Step 5: Set Up the Webhook

#### Option A — Use Webhook.site (for testing)
1. Go to [webhook.site](https://webhook.site) → copy your unique URL.
2. In Zapier Agent Tools → **"+ Add Tool"** → search **Webhooks by Zapier**.
3. Select **POST** action, paste the webhook.site URL.

#### Option B — Use a real downstream system URL
Replace with your own endpoint URL.

**Required JSON body structure (Zapier will auto-fill from agent output):**
```json
{
  "command_id": "CMD_20260128_001",
  "action": "ALERT",
  "severity": "HIGH",
  "reason": "PAYMENT step failure - critical revenue impact",
  "checkout_step": "PAYMENT",
  "cart_value": 4599,
  "device": "MOBILE",
  "baseline_rate": 9.8,
  "timestamp": "2026-01-28 13:30:00"
}
```

---

### Step 6: Set the Agent Trigger

1. In your Agent → **"Trigger"** section → choose **"Schedule"**.
2. Set to run every **1 hour** (or every 15 minutes for demo purposes).
3. Alternatively, use **"Manual"** trigger for testing.

---

### Step 7: Test the Agent

1. Make sure your State sheet's `last_processed_timestamp` is set to a time BEFORE your Cart_Events data (e.g., `2026-01-28 13:15:00`).
2. Click **"Run Agent"** manually in Zapier.
3. Watch the agent:
   - Read State → fetch new events → evaluate each one → write to Agent_Commands → fire webhook → update State.
4. Check your `Agent_Commands` sheet — new rows should appear.
5. Check webhook.site (if used) — you should see the POST requests arrive.

---

## PART 3 — DECISION LOGIC REFERENCE

### When does ALERT fire?

| Condition | Rule |
|---|---|
| PAYMENT step | Always HIGH — direct revenue loss |
| cart_value > $1,000 | HIGH — significant transaction at risk |
| Multiple MOBILE failures | HIGH — likely app/platform bug |
| Failure rate > baseline | HIGH — abnormal spike detected |

### When does LOG fire?

- Low cart value (< $1,000)
- Isolated incident on ADDRESS or SHIPPING
- No pattern of mobile failures
- Rate within baseline

### Example Decisions

| Event | Severity | Action | Reason |
|---|---|---|---|
| PAYMENT, $4,599, MOBILE | HIGH | ALERT | Payment step + high cart value + mobile |
| ADDRESS, $30, MOBILE | LOW | LOG | Low value, not payment step |
| SHIPPING, $1,199, DESKTOP | LOW | LOG | Not payment, low count |
| PAYMENT, $6,200, DESKTOP | HIGH | ALERT | Payment step + very high cart value |

---

## PART 4 — STATE MANAGEMENT FLOW

```
Run starts
    │
    ▼
Read State sheet → get last_processed_timestamp (e.g., 13:15:00)
    │
    ▼
Filter Cart_Events → only rows where timestamp > 13:15:00
    │
    ├─ No new rows → Write LOG "No new events" → STOP
    │
    ▼
For each new row:
    Evaluate severity (HIGH / LOW)
    → Write 1 row to Agent_Commands
    → POST webhook
    │
    ▼
Update State sheet → last_processed_timestamp = latest event's timestamp
    │
    ▼
Run ends (next run will start from new timestamp)
```

**Zero Duplicates Guarantee:** Because State is always updated to the latest processed timestamp, the next run will never re-process old rows.

---

## PART 5 — CHECKLIST FOR SUBMISSION

- [ ] Google Sheets created with all 4 sheets (Cart_Events, Baseline_Metrics, State, Agent_Commands)
- [ ] Cart_Events has at least 10 rows of sample data
- [ ] Baseline_Metrics has all 3 steps with rates
- [ ] State sheet has `last_processed_timestamp` key
- [ ] Agent_Commands has the 9 required columns
- [ ] Zapier Agent created with full system prompt
- [ ] Google Sheets tool connected in Zapier
- [ ] Webhook configured and tested
- [ ] Agent run at least once successfully
- [ ] Agent_Commands sheet shows ALERT and LOG rows
- [ ] State sheet was updated after the run
- [ ] Webhook.site (or endpoint) shows received POST requests
- [ ] No duplicate rows in Agent_Commands
