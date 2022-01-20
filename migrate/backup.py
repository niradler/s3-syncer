import os
from subprocess import check_output

source_bucket = os.getenv(
    'SOURCE_BUCKET', 'na-test-1')
target_folder = os.getenv('TARGET_FOLDER', './data')
source_prefix = ''
exclude = []
include = []
region = os.getenv('AWS_DEFAULT_REGION', 'us-east-1')

sync_cmd = f'aws s3 sync s3://{source_bucket}{source_prefix} {target_folder} --region {region}'

if len(exclude) > 0:
    sync_cmd += ' --exclude ' + ' --exclude '.join(exclude)
if len(include) > 0:
    sync_cmd += ' --include ' + ' --include '.join(include)

print(f'running {sync_cmd}')
out = check_output(sync_cmd.split(' '))
print("output:")
print(out)
