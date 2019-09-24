#!/bin/bash

aws --endpoint-url=${AWS_S3_ENDPOINT_URL} s3api create-bucket --bucket ${AWS_BUCKET_NAME} --region eu-north-1
aws --endpoint-url=${AWS_S3_ENDPOINT_URL} s3api put-bucket-acl --bucket ${AWS_BUCKET_NAME} --acl public-read