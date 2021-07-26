# s3-syncer

2021 Lyve Cloud Hackathon.

Introducing a new approach to cloud storage. Lyve™ Cloud from Seagate® is your simple, trusted and efficient storage as a service. Long-term cost predictability means you’ll never be surprised by your cloud bill. Put your data to work with always-on availability, world-class security, and cloud flexibility from the global leader in mass data storage management.

What is s3-syncer?

s3 synchronization automation, deploy syncer to your aws account and connect to the bucket you wish to sync with Lyve Cloud storage.
using s3 notification syncer will reflect any change in the source bucket also in the target bucket and keep them in sync.

## Setup

- Step 0: make sure you have aws cli configure correctly
- Step 1: cd syncer && pip3 install -r requirements.txt && chalice deploy
- Step 2: log in to aws console and make sure the lambda we created have the needed permissions and the environment variables of SOURCE_BUCKET/TARGET_BUCKET configured correctly.
- Step 3: run syncer docker image, go to /migrate/README.md for more details (recommended run as ECS Fargate task, block s3 changes while syncing)

## TODO

- smart sync with thread pool and concurrent processes
- easier configuration
- run as a service
