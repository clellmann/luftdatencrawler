import requests
import boto3
import os

API = 'http://api.luftdaten.info/static/v1/data.json'


def filter_pm_data(json):
    """
    Filters only sensors with PM data.
    Args:
        json (list): List of sensor data jsons.

    Returns (list): List of filtered sensor data jsons.

    """
    return [elem for elem in json if any([True if 'P1' in data.values() or 'P2' in data.values() else False for data in elem['sensordatavalues']])]


if __name__=='__main__':
    res = requests.get(API).json()
    sensordata = filter_pm_data(res)
    dynamodb = boto3.resource('dynamodb', region_name='us-west-1', aws_access_key_id=os.environ['ACCESS_KEY'], aws_secret_access_key=os.environ['SECRET'])
    table = dynamodb.Table('luftdaten')
    for sensordate in sensordata:
        table.put_item(Item=sensordate)
