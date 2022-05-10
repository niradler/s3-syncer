import os
from subprocess import check_output

source_bucket = os.getenv('SOURCE_BUCKET', 'aws-bucket')
target_bucket = os.getenv('TARGET_BUCKET', 'lyvecloud-bucket')
source_prefix = ''
exclude = []
include = []
region = os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
endpoint = os.getenv('ENDPOINT', 'https://s3.us-east-1.lyvecloud.seagate.com')
sync_cmd = f'aws s3 sync s3://{source_bucket}{source_prefix} s3://{target_bucket}{source_prefix} --region {region} --endpoint-url {endpoint}'

if len(exclude) > 0:
    sync_cmd += ' --exclude ' + ' --exclude '.join(exclude)
if len(include) > 0:
    sync_cmd += ' --include ' + ' --include '.join(include)

print(f'running {sync_cmd}')
out = check_output(sync_cmd.split(' '))
print("output:")
print(out)
