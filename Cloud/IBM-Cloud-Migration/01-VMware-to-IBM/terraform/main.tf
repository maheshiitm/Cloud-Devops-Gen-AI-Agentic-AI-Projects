terraform {
  required_version = '>= 1.5.0'

  required_providers {
    ibm = {
      source = 'IBM-Cloud/ibm'
      version = '~> 1.78'
    }
  }
}

provider 'ibm' {
  region = var.region
}

resource 'ibm_is_vpc' 'migration' {
  name = '-vpc'
}

output 'vpc_id' {
  value = ibm_is_vpc.migration.id
}
