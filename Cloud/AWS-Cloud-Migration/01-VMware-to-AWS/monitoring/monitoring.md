# Monitoring and Observability

## Infrastructure Monitoring

Monitor:

- EC2 CPU
- Memory
- Disk
- Network
- EBS
- Load Balancer
- Auto Scaling
- EFS
- Application availability

## Application Monitoring

Monitor:

- HTTP response codes
- Response time
- Error rate
- Application logs
- Authentication failures
- Transaction failures

## AWS Services

Recommended services:

- Amazon CloudWatch
- CloudWatch Logs
- CloudWatch Alarms
- AWS CloudTrail
- AWS Systems Manager
- SNS

## Alert Categories

### Critical

Immediate operational response required.

### Warning

Investigate during normal operational process.

### Informational

Used for reporting and audit purposes.

## Example Alerts

- EC2 CPU > 80%
- Application health check failure
- ALB 5xx errors
- Disk utilization > 80%
- Instance status check failure
- Unexpected security events
