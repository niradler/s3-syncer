aws s3api create-bucket --bucket sync-test-2
aws s3api create-bucket --bucket sync-test-3
cd syncer && pip3 install -r requirements.txt && chalice deploy
