import boto3
import json

session = boto3.Session(profile_name='<aws-profile>')
sns_client = session.client('sns')

# Messages are often json
message = {
    'item': 'Latte',
    'total': 2.25
}

response = sns_client.publish(
    TargetArn='<topic-arn>',
    Message=json.dumps({'default': json.dumps(message)}),
    MessageStructure='json'
)

print(f'response = {response}')
