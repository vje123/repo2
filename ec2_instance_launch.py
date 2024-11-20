import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Parameters for the instance

ami_id = "ami-02a2af70a66af6dfb"  # Replace with your preferred AMI ID
instance_type = "t2.micro"
key_name = "jenny"  # Replace with your key pair name
security_group = "jenny-katre"  # Replace with your security group ID

# Launch the instance
response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroupIds=[security_group],
    MinCount=1,
    MaxCount=1
)

# Get the instance ID
instance_id = response['Instances'][0]['InstanceId']
print(f"EC2 Instance launched! Instance ID: {instance_id}")

ec2.create_tags(
    Resources=[instance_id],
    Tags=[
        {'Key': 'Name', 'Value': 'MyEC2Instance'}
    ]
)
print("Tag 'Name: MyEC2Instance' added to the instance.")
