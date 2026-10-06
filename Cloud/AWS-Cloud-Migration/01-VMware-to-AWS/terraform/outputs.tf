output "vpc_id" {
  description = "Migration VPC ID"
  value       = aws_vpc.migration.id
}

output "public_subnet_ids" {
  description = "Public subnet IDs"
  value       = aws_subnet.public[*].id
}

output "availability_zones" {
  description = "Configured availability zones"
  value       = var.availability_zones
}
