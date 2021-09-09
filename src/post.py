import json
import boto3


def handler(event, context):

    client = boto3.resource('dynamodb')
    table = client.Table("service")
    
    table.put_item(
        Item={
            'image_id': event['image_id'],
            'first_name': event['first_name'],
            'last_name': event['last_name'],
            'balance': event['balance'],
            'phone_number': event['phone_number']
        }    
    )
    
    data = table.scan()['Items']
    print("table ", table.table_status)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": f"data: ,{data}",
            }
        ),
    }