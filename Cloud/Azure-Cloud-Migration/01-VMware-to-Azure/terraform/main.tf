terraform {
  required_version = ">= 1.5.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }
}

provider "azurerm" {
  features {}
}

variable "location" {
  default = "Central India"
}

variable "resource_group_name" {
  default = "rg-vmware-migration"
}

resource "azurerm_resource_group" "migration" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_virtual_network" "migration" {
  name                = "vnet-vmware-migration"
  address_space       = ["10.20.0.0/16"]
  location            = azurerm_resource_group.migration.location
  resource_group_name = azurerm_resource_group.migration.name
}

resource "azurerm_subnet" "app" {
  name                 = "app-subnet"
  resource_group_name  = azurerm_resource_group.migration.name
  virtual_network_name = azurerm_virtual_network.migration.name
  address_prefixes     = ["10.20.1.0/24"]
}

output "resource_group_name" {
  value = azurerm_resource_group.migration.name
}

output "vnet_name" {
  value = azurerm_virtual_network.migration.name
}
