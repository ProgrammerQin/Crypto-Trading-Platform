# This python file to configure NoSQL Database and test connection

#   install boto3
import boto3
from botocore.config import Config

my_config = Config(
    region_name = 'us-east-2',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

client = boto3.client('kinesis', config=my_config)

s3 = boto3.resource('s3', region_name='us-east-2')
dynamodb = boto3.client('dynamodb')


table = dynamodb.table('ETH_Trading_Graph')
print(table.creation_date_time)

