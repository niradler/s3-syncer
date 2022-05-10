from chalice import Chalice
import os
import boto3
from botocore.client import Config

# Lyve Cloud
s3_resource = boto3.resource('s3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID', 'TEST_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_ACCESS_KEY_SECRET', 'TEST_KEY_SECRET'),
    region_name=os.getenv('AWS_DEFAULT_REGION', 'TEST_REGION'),
    config=Config(signature_version='s3v4'),
    endpoint_url='TEST_ENDPOINT_URL'
)

# Lyve Cloud
s3_client = boto3.client('s3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID', 'TEST_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_ACCESS_KEY_SECRET', 'TEST_KEY_SECRET'),
    region_name=os.getenv('AWS_DEFAULT_REGION', 'TEST_REGION'),
    config=Config(signature_version='s3v4'),
    endpoint_url='TEST_ENDPOINT_URL'
)

sourceS3 = boto3.resource('s3')
app = Chalice(app_name='syncer', debug=True)
source_bucket = os.getenv('SOURCE_BUCKET', 'aws-bucket')
target_bucket = os.getenv('TARGET_BUCKET', 'lyvecloud-bucket')
source_prefix = ''


@app.on_s3_event(bucket=source_bucket, prefix=source_prefix, events=['s3:ObjectCreated:*'])
def handle_create_object(event):
    event_dic = event.to_dict()
    app.log.info(event_dic)
    action_name = event_dic['Records'][0]['eventName']
    size = event_dic['Records'][0]['s3']['object']['size']
    app.log.info("Event received for bucket: %s, key %s, eventName %s, size %s", event.bucket, event.key, action_name, size)

    if size > 0:
        app.log.info("create sync start")
        app.log.info(source_bucket)
        bucket = sourceS3.Bucket(source_bucket)
        file_path = '/tmp/'+event.key
        app.log.info(file_path)
        bucket.download_file(event.key, file_path)
        app.log.info("downloaded file")
        bucket = s3_resource.Bucket(target_bucket)
        bucket.upload_file(file_path, event.key)
        app.log.info("create sync complete")


@app.on_s3_event(bucket=source_bucket, prefix=source_prefix, events=['s3:ObjectRemoved:*'])
def handle_remove_object(event):
    event_dic = event.to_dict()
    app.log.info(event_dic)
    action_name = event_dic['Records'][0]['eventName']
    app.log.info("Event received for bucket: %s, key %s, eventName %s", event.bucket, event.key, action_name)
    app.log.info("remove sync start")
    s3_client.delete_object(Bucket=target_bucket, Key=event.key)
    app.log.info("remove sync complete")
