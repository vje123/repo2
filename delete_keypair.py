import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2', region_name="ap-south-1")

# Key pair name
key_name = "jenny"

# Delete the key pair
response = ec2.delete_key_pair(KeyName=key_name)
print(f"Key pair '{key_name}' deleted successfully.")





