# Import all the modules and libraries
import boto3

# Import pprint
from pprint import pprint

# Open the Management Console
aws_management_console = boto3.session.Session(profile_name="default")
# Open IAM Console
iam_console = aws_management_console.client(service_name="iam")
# Use Boto3 Documentaion to get more information (https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html)
# Create a variable (result)
result = iam_console.list_users()

# Then, print result
pprint(result)
