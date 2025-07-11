import boto3
import json

session = boto3.Session(profile_name='<aws-profile>')
sqs_client = session.client('sqs')

# Messages are often json
message = {
    'item': 'Hot CHocolate',
    'total': 3.25
}

response = sqs_client.send_message(
    QueueUrl='<url-of-the-queue>',
    MessageAttributes={
        'Author': {
            'StringValue': '<your-name>',
            'DataType': 'String'
        }
    },
    MessageBody=json.dumps(message)
)

print(f'response = {response}')
