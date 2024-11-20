import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2', region_name="ap-south-1")

# List of instance IDs to terminate
instance_ids = ["i-02312e8d139e2ed41", "i-08319372a00da7312"]

# Terminate instances
response = ec2.terminate_instances(InstanceIds=instance_ids)
print("Termination initiated for instances:")
for instance in response['TerminatingInstances']:
    print(f"Instance ID: {instance['InstanceId']}, State: {instance['CurrentState']['Name']}")
