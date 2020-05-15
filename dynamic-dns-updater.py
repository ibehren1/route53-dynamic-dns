#!/usr/bin/env python3

import boto3
import json
import requests

from botocore.exceptions import ClientError

# Update these two variables with your domain name and DNS record.
domain_name = "example.com"
dns_record = "gateway.example.com"

route53 = boto3.client('route53')


def get_current_ip():
    url = 'https://ifconfig.co/json'
    r = requests.get(url)
    data = json.loads(r.text)
    return data['ip']


def get_hosted_zone_id():
    response = route53.list_hosted_zones_by_name(DNSName=domain_name + '.')
    hosted_zone_id = response['HostedZones'][0]['Id']
    hosted_zone_id = hosted_zone_id.split("/", 2)[2]
    return hosted_zone_id


def get_dns_ip():
    response = route53.list_resource_record_sets(
        HostedZoneId=get_hosted_zone_id(),
        StartRecordName=dns_record,
        StartRecordType='A',
        MaxItems='1'
    )
    return response['ResourceRecordSets'][0]['ResourceRecords'][0]['Value']


def update_dns_record(current_ip):
    try:
        route53.change_resource_record_sets(
            HostedZoneId=get_hosted_zone_id(),
            ChangeBatch={
                'Changes': [
                    {
                        'Action': 'UPSERT',
                        'ResourceRecordSet': {
                            'Name': dns_record,
                            'Type': 'A',
                            'TTL': 60,
                            'ResourceRecords': [
                                {
                                    'Value': current_ip
                                },
                            ],
                        }
                    },
                ]
            }
        )
    except ClientError:
        print('Failed to update Route53 DNS record.')
    print(dns_record + ' updated to ' + current_ip)


def main():
    current_ip = get_current_ip()
    current_dns_ip = get_dns_ip()

    if current_ip == current_dns_ip:
        print('No update needed.')
    else:
        update_dns_record(current_ip)


if __name__ == "__main__":
    main()
