#!/bin/bash
set -e

echo "Azure VMware migration deployment started"

cd terraform
terraform init
terraform validate
terraform plan

echo "Deployment plan completed"
