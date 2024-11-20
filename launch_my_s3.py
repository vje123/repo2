import boto3

# Create a session using boto3
session = boto3.Session()

# Get the S3 client
s3 = session.client('s3')

# List all buckets
response = s3.list_buckets()

# Print bucket names
print("Buckets in your AWS account:")
for bucket in response['Buckets']:
    print(f"  - {bucket['Name']}")
