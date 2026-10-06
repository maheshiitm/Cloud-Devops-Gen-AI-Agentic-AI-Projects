variable "aws_region" {
  description = "AWS region for the migration target"
  type        = string
  default     = "ap-south-1"
}

variable "project_name" {
  description = "Migration project name"
  type        = string
  default     = "vmware-to-aws"
}

variable "vpc_cidr" {
  description = "CIDR block for the migration VPC"
  type        = string
  default     = "10.10.0.0/16"
}

variable "availability_zones" {
  description = "Availability zones"
  type        = list(string)
  default = [
    "ap-south-1a",
    "ap-south-1b"
  ]
}
