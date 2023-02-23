import json
import requests

def lambda_handler(event, context):
    # TODO implement
    return {
        'headers': {'Content-Type' : 'application/json'},
        'statusCode': 200,
        'body': json.dumps('Hello World from Lambda!')
    }
