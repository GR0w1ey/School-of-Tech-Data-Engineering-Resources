import boto3
import json

session = boto3.Session(profile_name='sot-academy')
sqs_client = session.client('sqs')

message = { "item": "latte", "price": 2.25 }

queue_url = "https://sqs.eu-west-1.amazonaws.com/745580839125/gregor-rowley-coffee-sales-queue"

response = sqs_client.send_message(
    QueueUrl = queue_url,
    MessageAttributes={
        'Author': {
            'StringValue': 'Gregor Rowley',
            'DataType': 'String'
        }
    },
    MessageBody=json.dumps(message)
)

print(f'response = {response}')
