# ☁️ Upload raw article data to AWS S3
import boto3
import json
import os
from dotenv import load_dotenv

# Load credentials from .env file
load_dotenv()
bucket = os.getenv("AWS_S3_BUCKET")

def upload_to_s3(data, filename):
    try:
        s3 = boto3.client("s3")
        s3.put_object(Bucket=bucket, Key=filename, Body=json.dumps(data))
        print(f"Uploaded {filename} to S3 bucket {bucket}")
    except Exception as e:
        print(f"Upload failed: {e}")
