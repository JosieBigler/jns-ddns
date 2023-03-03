import boto3
from botocore.exceptions import ClientError

def update_ip(new_ip):
    session = boto3.Session(
        aws_access_key_id='AKIAXORAA2BDBEVWF7XI',
        aws_secret_access_key='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'
    )

    client = session.client('route53')
    hosted_zone_id = 'Z0736001OTNYT18XKCM6'
    domain_name = 'home.jnsfullstack.com'
    changes = {
        'Changes': [
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': domain_name,
                    'Type': 'A',
                    'TTL': 300,
                    'ResourceRecords': [{'Value': new_ip}]
                }
            }
        ]
    }

    try:
        response = client.change_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            ChangeBatch=changes
        )
        print('A record updated successfully')
    except ClientError as e:
        print(e)