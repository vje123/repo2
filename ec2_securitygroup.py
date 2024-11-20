import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Security group details
group_name = "jenny-katre"
description = "Security group for vijay EC2 instance"

# Create the security group
response = ec2.create_security_group(GroupName=group_name, Description=description)
security_group_id = response['GroupId']

# Add rules to allow SSH (port 22) and HTTP (port 80) access
ec2.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 22,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]  # SSH access from anywhere
        },
        {
            'IpProtocol': 'tcp',
            'FromPort': 80,
            'ToPort': 80,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]  # HTTP access from anywhere
        }
    ]
)

print(f"Security group '{group_name}' created with ID: {security_group_id}")
