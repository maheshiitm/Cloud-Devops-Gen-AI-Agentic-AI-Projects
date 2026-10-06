# Cutover Plan

## Pre-Cutover

- Confirm migration approval.
- Confirm change window.
- Validate AWS infrastructure.
- Validate application dependencies.
- Validate backups.
- Confirm monitoring.
- Confirm rollback decision criteria.
- Notify stakeholders.

## Cutover

1. Announce start of change.
2. Stop application writes on VMware.
3. Perform final data synchronization.
4. Validate data.
5. Start AWS application.
6. Run health checks.
7. Run functional validation.
8. Enable production traffic.
9. Monitor application and infrastructure.

## Validation

- HTTP/HTTPS availability
- Application login
- Critical business transactions
- Database connectivity
- Storage connectivity
- Monitoring
- Logs
- Alerts

## Success Criteria

The migration is successful when:

- Application is reachable.
- Critical transactions work.
- No critical errors are observed.
- Performance is within agreed limits.
- Business owner confirms functionality.

## Communication

Migration status should be communicated at:

- Start
- Major milestone
- Validation
- Traffic switch
- Completion
