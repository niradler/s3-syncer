# s3-syncer

2021 Lyve Cloud Hackathon.

Introducing a new approach to cloud storage. Lyve™ Cloud from Seagate® is your simple, trusted and efficient storage as a service. Long-term cost predictability means you’ll never be surprised by your cloud bill. Put your data to work with always-on availability, world-class security, and cloud flexibility from the global leader in mass data storage management.

What is s3-syncer?

s3 synchronization automation, deploy syncer to your aws account and connect to the bucket you wish to sync with Lyve Cloud storage.
using s3 notification syncer will reflect any change in the source bucket also in the target bucket and keep them in sync.

## Sync Flow

### [1] Migration

copy all your files from one bucket to another [using aws cli sync command](https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html)
sync command can be stopped and run again, and diff check will be made.

#### Setup

use the docker file for simplified setup
(recommended run as ECS Fargate task, block s3 changes while syncing)

```
cd migrate
docker build . -t s3-migration
docker run --env AWS_DEFAULT_REGION=us-west-2  --env AWS_ACCESS_KEY_ID=us-west-2 --env AWS_SECRET_ACCESS_KEY=us-west-2 --env SOURCE_BUCKET=us-west-2 --env TARGET_BUCKET=us-west-2 --env ENDPOINT=https://s3.us-east-1.lyvecloud.seagate.com --rm s3-migration
```

### [2] Sync

keep your buckets in sync with changes happening.
the sync is made by s3 event trigger Craete/Remove => trigger syncer lambda function.
(for more robust solution use sqs to cache the events and add support to more events)

#### Setup

syncer is a lambda function base on python (3.8)

- Step 0: make sure you have [aws cli configure correctly](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
- step 1: update environment variable to match your environment (optional: AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY_SECRET, AWS_DEFAULT_REGION, required: SOURCE_BUCKET, TARGET_BUCKET)
- Step 2: cd syncer && pip3 install -r requirements.txt && chalice deploy
- Step 3: log in to aws console and make sure the lambda we created have the needed permissions and the environment variables of SOURCE_BUCKET/TARGET_BUCKET configured correctly.

## TODO

- smart sync with thread pool and concurrent processes
- easier configuration
- run as a service
- improve copy
- aws cli limitation to pass just one endpoint url (we need to use a buffer at the moment)

## Notes

- aws cli support to pass just one endpoint url (we need to use a buffer at the moment to copy from one bucket to another if endpoint is not the same)
- develop on windows machine and docker.

## Demo and examples

[sync video](https://www.loom.com/share/11e098376d8548ddb35a1f6ec4266e2e)

![sync](https://cdn.loom.com/sessions/thumbnails/11e098376d8548ddb35a1f6ec4266e2e-with-play.gif)

![Create object lambda](images/syncer_create.PNG?raw=true "Create object lambda")

![Remove object lambda](images/syncer_remove.PNG?raw=true "Remove object lambda")

![Remove object lambda](images/syncer_remove.PNG?raw=true "Remove object lambda")

![Buckets](images/syncer_remove.PNG?raw=true "Buckets")

![Logs](images/logs.PNG?raw=true "Logs")
