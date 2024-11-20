import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2', region_name="ap-south-1")
# Security group ID
security_group_id = "sg-04a2bde571cb6d8c7"

# Delete the security group
response = ec2.delete_security_group(GroupId=security_group_id)
print(f"Security group '{security_group_id}' deleted successfully.")
