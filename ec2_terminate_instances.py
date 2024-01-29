# Import all the modules and libraries
import boto3
# Open the Management Console
aws_management_console = boto3.session.Session(profile_name="default")
# Open EC2 Console
ec2_console = aws_management_console.client(service_name="ec2")

# Use Boto3 Documentaion to get more information (https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html)
response = ec2_console.terminate_instances(
    InstanceIds=['i-0d50f1d1793675e75']   
)