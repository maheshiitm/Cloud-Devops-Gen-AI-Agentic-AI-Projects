# VMware to Azure Architecture

Users
  |
Azure Load Balancer
  |
+----------------------+
|                      |
Azure VM 1          Azure VM 2
|                      |
+----------+-----------+
           |
      Azure Storage

Management:
Terraform -> Infrastructure as Code
Ansible -> Configuration Management
Docker -> Application Packaging
AKS -> Container Platform
Jenkins/GitHub Actions -> CI/CD
Azure Monitor -> Observability
