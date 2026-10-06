# VMware to AWS Migration Architecture

## Objective

Migrate a VMware-hosted application workload to AWS while maintaining availability, security, observability and rollback capability.

## Target Architecture

```text
                         Internet / Users
                                |
                                v
                     +----------------------+
                     | Application Load     |
                     | Balancer             |
                     +----------+-----------+
                                |
                    +-----------+-----------+
                    |                       |
                    v                       v
             +-------------+         +-------------+
             | EC2 App 01  |         | EC2 App 02  |
             | Private     |         | Private     |
             | Subnet      |         | Subnet      |
             +------+------+         +------+------+
                    |                       |
                    +-----------+-----------+
                                |
                    +-----------+-----------+
                    |                       |
                    v                       v
                  EFS                       S3
             Shared Storage          Backup / Objects
                    |
                    v
             CloudWatch / SNS

Management Layer
----------------
Terraform       -> Infrastructure as Code
Ansible         -> Server Configuration
Docker          -> Application Packaging
Jenkins/GitHub  -> CI/CD
AWS Systems     -> Operations
Manager

Security Layer
--------------
IAM
Security Groups
Private Subnets
Encryption
CloudTrail
CloudWatch
Secrets Management
