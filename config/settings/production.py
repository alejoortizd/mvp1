import os

from .base import *  # noqa

STORAGES = {
    "default": {
        "BACKEND": "config.backends.StaticRootS3Boto3Storage",
        "OPTIONS": {
            "region_name": os.getenv("AWS_S3_REGION_NAME"),
            "endpoint_url": os.getenv("AWS_S3_ENDPOINT_URL"),
            "bucket_name": os.getenv("AWS_STORAGE_BUCKET_NAME"),
            "access_key": os.getenv("AWS_ACCESS_KEY_ID"),
            "secret_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
            "default_acl": "public-read",
        },
    },
    "staticfiles": {
        "BACKEND": "config.backends.StaticRootS3Boto3Storage",
        "OPTIONS": {
            "region_name": os.getenv("AWS_S3_REGION_NAME"),
            "endpoint_url": os.getenv("AWS_S3_ENDPOINT_URL"),
            "bucket_name": os.getenv("AWS_STORAGE_BUCKET_NAME"),
            "access_key": os.getenv("AWS_ACCESS_KEY_ID"),
            "secret_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
            "default_acl": "public-read",
        },
    },
}
