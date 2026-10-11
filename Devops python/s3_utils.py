import boto3

s3 = boto3.client('s3')

# for bucket in s3.buckets.all():
#     print(bucket.name)

file_name=r"C:\Padhai likhai\Python\Devops python\api.py"
object_name="api.py"
bucket = "nag3"

response = s3.upload_file(file_name,bucket,object_name)