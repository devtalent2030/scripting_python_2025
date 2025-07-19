from moto import mock_s3
import boto3
from aws_s3_audit import is_public

@mock_s3
def test_risk_detection():
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket="public-bkt")
    # default ACL exposes AllUsers READ
    assert is_public(s3, "public-bkt") is True
