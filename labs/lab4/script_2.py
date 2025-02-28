import boto3
import requests
import sys
import os
    
file_url = sys.argv[1]
bucket_name = sys.argv[2]
expiration = int(sys.argv[3])

local_file = file_url.split("/")[-1]
response = requests.get(file_url, stream=True)
with open(local_file, 'wb') as file:
  for chunk in response.iter_content(1024):
    file.write(chunk)
    
s3_client = boto3.client('s3')
s3_client.upload_file(local_file, bucket_name, os.path.basename(local_file))

presigned_url = s3_client.generate_presigned_url('get_object',Params={'Bucket': bucket_name, 'Key': local_file},ExpiresIn=expiration)
print("Pre-signed URL:",presigned_url)
