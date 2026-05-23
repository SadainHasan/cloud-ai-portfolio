import json

def lambda_handler(event, context):
    print('Lambda triggered!')
    print(f'Event received: {json.dumps(event)}')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! Hasan Cloud Portfolio')
    }