#!/bin/bash

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Starting VMware-to-AWS deployment"

cd "$PROJECT_ROOT/terraform"

echo "Formatting Terraform"
terraform fmt -recursive

echo "Initializing Terraform"
terraform init

echo "Validating Terraform"
terraform validate

echo "Planning infrastructure"
terraform plan

echo "Deployment preparation completed."

echo "Review the Terraform plan before applying infrastructure."
