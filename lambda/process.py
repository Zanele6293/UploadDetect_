import json

def handler(event,context):
    for records in event['Records']:
        bucket_name= records['s3'['bucket']['name']]
        file_name = records['s3']['object']['key']
        print(f"File detected! Bucket: {bucket_name}, File: {file_name}")
    return{
        'statusCode': 200,
        'body':json.dumps('Cloud Function processed successfully!')
    }