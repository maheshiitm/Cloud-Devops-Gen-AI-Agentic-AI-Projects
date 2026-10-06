# VMware to IBM Cloud Architecture

VMware Environment
        |
        v
Migration Assessment
        |
        v
IBM Cloud VPC
        |
   +----+----+
   |         |
   v         v
IBM VM 1   IBM VM 2
   |         |
   +----+----+
        |
        v
IBM Cloud Object Storage
        |
        v
IBM Cloud Monitoring

Modernization: VMware -> Docker -> IKS

Automation: Terraform, Ansible, Jenkins, GitHub Actions
