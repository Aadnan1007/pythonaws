#configure aws using aws-cli command "aws configure"
#Create S3 bucket
import boto3
AWS_REGION = "us-east-2"
resource = boto3.resource("s3", region_name=AWS_REGION)
bucket_name = "adnanrtoc"
location = {'LocationConstraint': AWS_REGION}
bucket = resource.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration=location)

print("Amazon S3 bucket has been created")

#restrict s3 bucket access to specific ips
import json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "IPAllow",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": "arn:aws:s3:::$bucket_name/*",     #bucket_name/*
      "Condition": {
         "IpAddress": {"aws:SourceIp": ["54.240.143.0/24", "1.2.3.4/32" ]},
         "NotIpAddress": {"aws:SourceIp": "54.240.143.188/32"} 
      } 
    } 
  ]
}
