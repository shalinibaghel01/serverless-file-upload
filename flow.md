# 🔄 Project Execution Flow (Step-by-Step)

---

## 1. **S3 Bucket Creation**
- Created a new S3 bucket from the AWS Console.
- Gave it a unique name.
- Enabled **Event Notifications** in the S3 bucket settings.
- Configured a trigger for **PUT** events (when a file is uploaded).
- Lambda is set as the destination for the event trigger, so when a file is uploaded to the S3 bucket, it will trigger the Lambda function.

---

## 2. **IAM Role Creation for Lambda**
- Went to the IAM console and created a new role.
- **Trusted entity:** Lambda service (AWS Lambda was selected as the service that will use this role).
- **Attached the following permission policies:**
  - `AmazonS3FullAccess` – allows Lambda to read files from S3.
  - `AmazonDynamoDBFullAccess` – allows Lambda to write data to DynamoDB.
  - `CloudWatchLogsFullAccess` – allows Lambda to push logs to CloudWatch.
  - (Optional) Custom inline policy – for fine-tuned access to API Gateway or specific resources.

✅ This IAM role was later assigned to the Lambda function so that it could securely interact with AWS services.

---

## 3. **Lambda Function Setup**
- Created a new Lambda function (Name - FilesProcessed) :
  - Runtime: Python 3.10 (or your preferred runtime).
  - Assigned the IAM role created above to this Lambda function.
- Replaced the default code with custom logic to:
  - Extract metadata from uploaded files.
  - Store the metadata into a DynamoDB table.
- Configured S3 as the trigger for the Lambda function. Whenever a file is uploaded to S3, the Lambda function will be triggered automatically.

---

## 4. **DynamoDB Table Setup**
- Created a new DynamoDB table:
  - Table name: `FileMetadata`
  - Primary key: `filename` (String)
- The Lambda function uses the AWS SDK (`boto3`) to insert file metadata (File name, size, Upload time, Bucket name.) into this table when triggered by S3.

---

## 5. **API Gateway Integration with S3**
- Created a new REST API using API Gateway.
- Added a resource path `/upload` to the API.
- Added a **POST** method to the `/upload` resource.
- **Integration type:** **AWS Service** with **S3** as the service.
- **Action:** `s3:PutObject` – to allow API Gateway to upload files to the specified S3 bucket.
- **Resource:** `arn:aws:s3:::bucket-name/*` – specifies the target S3 bucket for the file upload.

---

## 6. **CloudWatch Monitoring**
- Since Lambda automatically integrates with CloudWatch, all logs from executions are captured there.
- Monitored the Lambda function logs for errors and performance metrics.
- Configured alarms in CloudWatch to trigger notifications when specific thresholds (e.g., error count) are reached.

---

## ✅ Overall Flow Summary

1. An HTTP POST request is sent to API Gateway at `/upload`.
2. API Gateway uploads the file to S3 using the `s3:PutObject` action.
3. Once the file is uploaded to S3, S3 triggers the Lambda function.
4. Lambda extracts metadata from the uploaded file (name, size, timestamp, etc.).
5. Lambda stores this metadata into a DynamoDB table.
6. Lambda logs the results to CloudWatch.
