#!/bin/bash
https://github.com/albertkangg/ds2002-pbp5hy/tree/main
LOCAL_FILE=$1
BUCKET_NAME=$2
EXPIRATION=$3

FILE_NAME=$(basename "$LOCAL_FILE")
aws s3 cp "$LOCAL_FILE" "s3://$BUCKET_NAME/$FILE_NAME" --acl private

PRESIGNED_URL=$(aws s3 presign "s3://$BUCKET_NAME/$FILE_NAME" --expires-in $EXPIRATION)

echo "Pre-signed URL: $PRESIGNED_URL"
