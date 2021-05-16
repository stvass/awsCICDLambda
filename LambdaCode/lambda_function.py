  
import boto3
import json


ec2 = boto3.client('ec2')
def lambda_handler(event, context):
    print("hi")
    response = 'Hello world'
    return {"statusCode": 200, "body": json.dumps(response)}