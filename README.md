# route53-dynamic-dns

Python script for doing dynamic DNS via Route53

## Requirements

- DNS hosted in AWS Route 53.
- Established host record to be checked and updated.
- Host with python3 to run update script on regular basis.

## Usage

Script is great for keeping your home's dynamic IP address updated without paying for a Dynamic DNS service.  Setup host to run script on a regular basis (via cron) and keep you public DNS record up to date.  Update two lines in the script with domain_name and dns_record and place on host.  Host should be setup with AWS credentials which have rights to read and write to  Route 53.

## AWS User/Policy via Terraform

In the terraform directory are the necessary Terraform templates to create a basic user and policy sufficient to read/update Route 53 and output the access key and secret.  To execute the Terraform code execute the following:

```bash
cd terraform
terraform init
terraform validate
terraform plan
terraform apply
```
