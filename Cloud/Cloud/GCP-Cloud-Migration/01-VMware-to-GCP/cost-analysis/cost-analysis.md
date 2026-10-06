# AWS Migration Cost Analysis

## Cost Model

This document provides a planning framework for estimating AWS migration costs.

The actual cost depends on:

- Number and size of EC2 instances
- Storage requirements
- Data transfer
- EBS volumes
- EFS usage
- Load balancer traffic
- CloudWatch metrics and logs
- Backup retention
- AWS support plan
- Region
- Reserved Instances or Savings Plans

## Example Workload

| Component | Example |
|---|---:|
| EC2 application servers | 2 |
| Application Load Balancer | 1 |
| EBS storage | 200 GB |
| EFS | 100 GB |
| S3 | 100 GB |
| CloudWatch | Enabled |
| Backup | Enabled |

## Cost Optimization

1. Right-size EC2 instances.
2. Use Auto Scaling where appropriate.
3. Use Savings Plans for stable workloads.
4. Apply S3 lifecycle policies.
5. Review EBS volumes regularly.
6. Monitor CloudWatch log retention.
7. Remove unused resources.
8. Use AWS Cost Explorer and budgets.

## Migration Cost Categories

### One-Time Costs

- Assessment
- Data transfer
- Migration tooling
- Engineering effort
- Testing
- Cutover

### Recurring Costs

- Compute
- Storage
- Network
- Monitoring
- Backup
- Security
- Support

Actual production pricing must be calculated using the AWS Pricing Calculator for the selected region and workload.
