# Cost Analysis

**Project:** CalendarMate\
**Student:** Mahesh P Zade

## 1. Cost Template Alignment

The assignment asks for: - LLM tokens per pipeline run. - Cost per
run. - Estimated runs/user/day. - Cost per user/day. - API calls. -
Observability cost. - Total estimated monthly cost/user.

## 2. Observed Evaluation Values

The supplied Langfuse report records a representative execution of
approximately:

  Item                    Observed value
  --------------------- ----------------
  Input tokens                   \~2,770
  Output tokens                    \~120
  Total tokens                   \~2,890
  Total latency                \~4.0 sec
  Time to first token         \~1.28 sec
  Observed cost/run         \~\$0.000286

The observed cost is the empirical figure reported by the supplied
Langfuse evidence.

## 3. Daily and Monthly Scenarios

Using the observed cost/run:

  Usage                            Calculation           Estimated cost
  -------------------------------- ------------------ -----------------
  15 runs/day                      15 × \$0.000286        \$0.00429/day
  30 runs/day                      30 × \$0.000286        \$0.00858/day
  30 runs/day × 20 business days   600 × \$0.000286     \$0.17160/month

These are estimates based on the observed evaluation trace, not a
provider quote.

## 4. Important Pricing Note

The workflow JSON identifies `gpt-4o-mini` and includes provider
metadata. Because model pricing can change and the observed Langfuse
cost is already available, this document treats the Langfuse-observed
cost as the primary empirical evaluation number.

Do not present an unverified historical price as a current provider
price.

## 5. API Costs

The Google Calendar and Gmail APIs generally depend on provider quotas
and usage. In the current validated capstone path, mock tools are used,
so live API charges are not part of the demonstrated baseline cost.

For production, include: - API usage/quota considerations. -
Infrastructure hosting. - Secret management. - Logging/observability. -
Network/egress if applicable.

## 6. Observability Cost

Langfuse is used for tracing. Actual production observability cost
depends on plan, retention, event volume, and configuration. For
capstone evaluation, the relevant evidence is that traces were captured
successfully.

## 7. Storage

The prototype does not require a dedicated persistent application
database for the validated mock workflow.

Production deployments may require: - User/application configuration. -
Audit metadata. - Secure token storage. - Optional historical data for
RAG.

## 8. Cost Optimization

-   Keep prompts concise and role-specific.
-   Route only to the required agent.
-   Limit unnecessary tool calls.
-   Use lower-cost models where quality permits.
-   Cache safe, reusable metadata.
-   Monitor token consumption with Langfuse.
-   Add evaluation gates before increasing model size.

## 9. Scaling

At scale, total cost is approximately:

`Users × requests/user/day × cost/request × active days`

Infrastructure and observability should be added to this model for
production budgeting.

## 10. Business Value

A planning scenario can compare system cost with time saved. For
example, if 50 users each recover 2 hours/day and the planning value of
an hour is \$150:

`50 × 2 × $150 × 20 = $300,000/month`

This is a planning/ROI scenario, not a measured production result.

## 11. Conclusion

The capstone prototype demonstrates a low per-run model cost under the
supplied evaluation conditions. Production budgeting should be revisited
using current provider pricing, real usage, live API usage, hosting, and
observability retention.
