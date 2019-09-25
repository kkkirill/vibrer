import os

import boto3


class FileUploaderS3:
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_S3_ENDPOINT_URL = os.environ['AWS_S3_ENDPOINT_URL']
    AWS_BUCKET_NAME = os.environ['AWS_BUCKET_NAME']

    def __init__(self) -> None:
        self.s3 = boto3.client('s3',
                               aws_access_key_id=self.AWS_ACCESS_KEY_ID,
                               aws_secret_access_key=self.AWS_SECRET_ACCESS_KEY,
                               endpoint_url=self.AWS_S3_ENDPOINT_URL)

    def upload_file_to_s3(self, file_name, key=None):
        if not key:
            key = file_name
        self.s3.upload_file(Filename=file_name,
                            Bucket=self.AWS_BUCKET_NAME, Key=key)
        return key

    def head_object(self, key):
        response = self.s3.head_object(Bucket=self.AWS_BUCKET_NAME, Key=key)
        return response

    def delete_file(self, key):
        response = self.s3.delete_object(Bucket=self.AWS_BUCKET_NAME, Key=key)
        return response