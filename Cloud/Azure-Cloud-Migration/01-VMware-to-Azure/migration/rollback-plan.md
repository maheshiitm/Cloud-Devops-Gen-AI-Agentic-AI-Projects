# Rollback Plan

Rollback triggers:
- Application failure
- Data integrity issue
- Performance degradation
- Security issue
- Critical dependency failure

Rollback:
1. Stop Azure application traffic.
2. Restore traffic to VMware.
3. Validate application health.
4. Preserve Azure logs for analysis.
5. Identify root cause.
6. Correct the issue.
7. Repeat migration after approval.
