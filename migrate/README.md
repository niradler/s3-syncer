# s3-migration

run the dockerfile with the following environment variables:

- AWS_DEFAULT_REGION
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- SOURCE_BUCKET
- SOURCE_FOLDER
- TARGET_BUCKET
- TARGET_FOLDER
- ENDPOINT

you can adjust sync filter by editing include/exclude in migrate/sync/py

the sync process will handle diff changes and will not copy object that already exist in the target bucket.

## Endpoint limitations

due to the lack of support for more then one endpoint, without modifying the aws cli, you need to do the migration in 2 steps:

```
docker build -t s3syncer .
docker run --name s3syncer --rm -i -t s3syncer bash
export AWS_DEFAULT_REGION=us-east-1
export AWS_ACCESS_KEY_ID=KEY
export AWS_SECRET_ACCESS_KEY=SECERT
export SOURCE_BUCKET=syncer
export SOURCE_FOLDER=/data
export TARGET_FOLDER=/data
export TARGET_BUCKET=syncer
python backup.py
export AWS_ACCESS_KEY_ID=KEY
export AWS_SECRET_ACCESS_KEY=SECERT
export ENDPOINT=ENDPOINT
python restore.py
```

2.
