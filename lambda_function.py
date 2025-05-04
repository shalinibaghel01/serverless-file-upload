import json
import boto3
import os
from datetime import datetime

# Initialize boto3 clients for DynamoDB and S3
dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

# Reference to the DynamoDB table
table_name = os.environ['DYNAMODB_TABLE_NAME']  # The table name from environment variables
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    # Extracting bucket name and file name from the S3 event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    file_size = event['Records'][0]['s3']['object']['size']
    
    # Get the current time when the file is uploaded (upload timestamp)
    upload_time = datetime.now().isoformat()  # This gives the current time in ISO 8601 format
    
    try:
        # Log the extracted metadata for debugging purposes
        print(f"File Details: Filename: {file_name}, Bucket: {bucket_name}, Size: {file_size}, Upload Time: {upload_time}")
        
        # Insert metadata into DynamoDB
        response = table.put_item(
            Item={
                'filename': file_name,  # Primary key (filename)
                'size': file_size,  # File size
                'upload_time': upload_time,  # Time of upload
                'bucket_name': bucket_name  # S3 bucket name
            }
        )
        
        # Log the response from DynamoDB
        print(f"Successfully inserted metadata into DynamoDB: {json.dumps(response)}")

        return {
            'statusCode': 200,
            'body': json.dumps('Metadata successfully stored in DynamoDB')
        }
    
    except Exception as e:
        # Log any error that occurs during the process
        print(f"Error: {str(e)}")
        
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error storing metadata: {str(e)}")
        }
