# Security Architecture

## Identity and Access Management

Follow least-privilege access.

Recommended controls:

- IAM roles instead of long-lived access keys.
- MFA for privileged users.
- Separate administrative and operational roles.
- Regular access reviews.

## Network Security

- Use private subnets for application servers.
- Restrict security group ingress.
- Avoid unrestricted SSH access.
- Use controlled administrative access.
- Use HTTPS for application traffic.

## Data Protection

- Encrypt EBS volumes.
- Encrypt EFS.
- Encrypt S3 objects.
- Protect backups.
- Use appropriate KMS keys.

## Secrets

Never commit:

- Passwords
- Private keys
- AWS access keys
- API tokens
- Production credentials

Use AWS Secrets Manager or AWS Systems Manager Parameter Store.

## Logging and Audit

Enable:

- CloudTrail
- CloudWatch Logs
- Security monitoring
- Authentication logging

## Migration Security

Before cutover:

- Validate firewall rules.
- Validate IAM permissions.
- Validate encryption.
- Validate backup.
- Validate monitoring.
- Review exposed ports.

## Compliance

The final implementation must be reviewed against the organization's applicable security and compliance requirements.
