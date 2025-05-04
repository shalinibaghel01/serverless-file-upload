# 📐 AWS Architecture Explanation

This project uses a combination of AWS serverless services to build an automatic file upload and processing system. Here's how each service contributes:

---

## ✅ AWS Services Used

### 1. **S3 (Simple Storage Service)**
- Acts as the storage layer.
- Files are uploaded directly to this bucket.
- Triggers an event whenever a file is uploaded.

### 2. **Lambda**
- Executes backend logic automatically without needing a server.
- Triggered by the S3 upload event.
- Processes the uploaded file and extracts metadata (file name, size, Upload time, Bucket name).
- Saves metadata to DynamoDB.

### 3. **DynamoDB**
- A NoSQL database.
- Stores file information such as:
  - File name
  - Size
  - Upload time
  - Bucket name

### 4. **IAM (Identity and Access Management)**
- Grants secure permissions to services.
- Lambda gets access to S3 and DynamoDB through IAM roles.
- API Gateway get access to S3 through IAM role policy created.

### 5. **API Gateway**
- Used to create a REST endpoint like `/upload`.
- Connects with S3(Simple Storage Service).
- Can be used by users to upload files through API instead of directly going to S3.

### 6. **CloudWatch**
- Used for monitoring logs.
- Tracks Lambda executions.
- Alarms can be configured for errors or performance tracking.

---

## 🧩 Integration Flow

- S3 triggers Lambda → Lambda processes → Data saved to DynamoDB → Logs go to CloudWatch
