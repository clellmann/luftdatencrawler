import boto3
import os

dynamodb = boto3.resource('dynamodb', region_name='us-west-1', aws_access_key_id=os.environ['ACCESS_KEY'], aws_secret_access_key=os.environ['SECRET'])
table = dynamodb.Table('luftdaten')
scan = table.scan(
    ProjectionExpression='#k',
    ExpressionAttributeNames={
        '#k': 'id'
    }
)
with table.batch_writer() as batch:
    for each in scan['Items']:
        batch.delete_item(Key=each)
