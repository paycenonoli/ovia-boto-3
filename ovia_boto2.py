import boto3
s3 = boto3.resource("s3")
dir(s3)
print(s3.get_available_subresources())

