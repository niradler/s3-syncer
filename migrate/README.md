# s3-migration

run the dockerfile with the following environment variables:

- AWS_DEFAULT_REGION
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- SOURCE_BUCKET
- TARGET_BUCKET
- ENDPOINT

you can adjust sync filter by editing include/exclude in migrate/sync/py

the sync process will handle diff changes and will not copy object that already exist in the target bucket.
