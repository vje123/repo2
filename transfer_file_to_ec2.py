import paramiko
from scp import SCPClient  # Correct import

# EC2 instance details
key_path = "jenny.pem"  # Path to your private key file
user = "ec2-user"
public_ip = "13.126.21.42"

# File paths
local_file = "/Users/vijaykumar/Documents/pic.jpeg"
remote_path = "/var/www/html/pic.jpeg"

# Set up SSH connection
key = paramiko.RSAKey.from_private_key_file(key_path)
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=public_ip, username=user, pkey=key)

# Transfer file using SCP
with SCPClient(ssh_client.get_transport()) as scp:
    scp.put(local_file, remote_path)

print(f"File {local_file} transferred to {remote_path}.")
ssh_client.close()
