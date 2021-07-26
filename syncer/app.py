from chalice import Chalice
import os
import boto3

s3 = boto3.resource('s3')

app = Chalice(app_name='syncer', debug=True)

source_bucket = os.getenv(
    'SOURCE_BUCKET', 'prod-policyerorg-platform-users-data')
target_bucket = os.getenv('TARGET_BUCKET', 'nit-test-bucket')
source_prefix = ''


@app.on_s3_event(bucket=source_bucket, prefix=source_prefix, events=['s3:ObjectCreated:*'])
def handle_create_object(event):
    event_dic = event.to_dict()
    action_name = event_dic['Records'][0]['eventName']
    size = event_dic['Records'][0]['s3']['object']['size']
    app.log.info("Event received for bucket: %s, key %s, eventName %s, size %s",
                 event.bucket, event.key, action_name, size)
    if size > 0:
        app.log.info("create sync start")
        copy_source = {
            'Bucket': source_bucket,
            'Key': event.key
        }
        bucket = s3.Bucket(target_bucket)
        bucket.copy(copy_source, event.key)
        app.log.info("create sync complete")

@app.on_s3_event(bucket=source_bucket, prefix=source_prefix, events=['s3:ObjectRemoved:*'])
def handle_remove_object(event):
    event_dic = event.to_dict()
    action_name = event_dic['Records'][0]['eventName']
    size = event_dic['Records'][0]['s3']['object']['size']
    app.log.info("Event received for bucket: %s, key %s, eventName %s, size %s",
                 event.bucket, event.key, action_name, size)
    if size > 0:
        app.log.info("remove sync start")
        bucket = s3.Bucket(target_bucket)
        bucket.remove(event.key)
        app.log.info("remove sync complete")