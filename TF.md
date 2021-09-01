# Best practices for Terraform
1. One workspace per environment per terraform configuration 
2. Running terraform fmt to format terraform configuration files and make them neat.
3.  Keep updating to latest terraform version using ```terraform init``` 
4. Validate and format terraform code before "applying" using
```
terraform validate
terraform fmt -check=true -write=false -diff=true
```