# Import boto3
import boto3
# Let's use Amazon S3
s3 = boto3.resource("s3")
# Print out bucket names in your account
for bucket in s3.buckets.all():
    print(bucket.name)
    
# Create an IAM client
iam = boto3.client("iam")

# List IAM users
response = iam.list_users()

# Print user details
# print(response)

print("IAM Users:")
for user in response['Users']:
    print(f"Username: {user['UserName']}")
    print(f"User ARN: {user['Arn']}")
    print(f"User ID: {user['UserId']}")
    
