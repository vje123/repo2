import boto3
import paramiko

# EC2 instance details
instance_id = "i-02312e8d139e2ed41"
key_path = "jenny.pem"  # Path to your private key file
user = "ec2-user"  # Default user for Amazon Linux 2

# Commands to run on the EC2 instance
commands = [
    "sudo yum update -y",
    "sudo yum install -y httpd",  # Install Apache HTTP server
    "sudo systemctl start httpd",
    "sudo systemctl enable httpd"
]

# Connect to EC2 instance
ec2 = boto3.client('ec2', region_name="ap-south-1")
response = ec2.describe_instances(InstanceIds=[instance_id])
instance = response['Reservations'][0]['Instances'][0]
public_ip = instance['PublicIpAddress']

print(f"Connecting to {public_ip}...")

# Set up SSH connection
key = paramiko.RSAKey.from_private_key_file(key_path)
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=public_ip, username=user, pkey=key)

# Run commands on EC2 instance
for cmd in commands:
    stdin, stdout, stderr = ssh_client.exec_command(cmd)
    print(stdout.read().decode())
    print(stderr.read().decode())

print("Dependencies installed and web server started!")
ssh_client.close()
