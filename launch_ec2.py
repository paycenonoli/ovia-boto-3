# Import all the modules and libraries
import boto3
# Open the Management Console
aws_management_console = boto3.session.Session(profile_name="ovia-terraform")
# Open EC2 Console
ec2_console = aws_management_console.client(service_name="ec2")

# Use Boto3 Documentaion to get more information (https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html)
response = ec2_console.run_instances(
    ImageId='ami-05fb0b8c1424f266b',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1
) 