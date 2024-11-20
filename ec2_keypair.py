import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Name of the key pair
key_pair_name = "jenny"

# Create the key pair
response = ec2.create_key_pair(KeyName=key_pair_name)

# Save the private key to a file
private_key = response['KeyMaterial']
with open(f"{key_pair_name}.pem", "w") as file:
    file.write(private_key)

print(f"Key pair '{key_pair_name}' created and saved as {key_pair_name}.pem")
