import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    print('event: ', event)
    client = boto3.resource('dynamodb')
    table = client.Table("service")

    try:
        response = table.scan()["Items"]
        print("response: ", response)
    
    except ClientError as e:
        print(e.response['Error']['Message'])

    return response