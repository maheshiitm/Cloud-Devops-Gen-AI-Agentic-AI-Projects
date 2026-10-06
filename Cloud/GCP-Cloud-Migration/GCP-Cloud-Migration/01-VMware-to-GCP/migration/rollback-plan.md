# Rollback Plan

## Rollback Trigger

Rollback may be initiated when:

- Critical application functionality fails.
- Data integrity is compromised.
- Performance is unacceptable.
- Security issue is identified.
- Critical dependency fails.
- Recovery criteria are not met within the agreed window.

## Rollback Procedure

1. Stop production traffic to AWS.
2. Preserve logs and evidence.
3. Restore traffic to VMware.
4. Validate VMware application.
5. Confirm data consistency.
6. Monitor application.
7. Notify stakeholders.
8. Open incident/problem record.
9. Perform root cause analysis.

## Rollback Decision Authority

Rollback should be approved by the designated:

- Application Owner
- Migration Lead
- Infrastructure Lead
- Business Owner

## Post-Rollback

- Document reason.
- Preserve evidence.
- Review monitoring.
- Identify corrective actions.
- Update migration plan.
- Schedule remediation before retry.
