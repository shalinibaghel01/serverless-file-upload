  Serverless File Upload Application          |
                                                               
 This project demonstrates a serverless file upload system     
 using AWS services: S3, Lambda, DynamoDB, API Gateway, and    
 CloudWatch.                                                   
                                                              
 Services Used:                                                
 - **S3**: Stores uploaded files.                              
 - **Lambda**: Processes file uploads and extracts metadata.   
 - **DynamoDB**: Stores file metadata.                         
 - **API Gateway**: Exposes an endpoint for file uploads.      
 - **CloudWatch**: Logs and monitors activities.               
                                                               
 Flow:                                                        
 1. **Upload**: Files are uploaded via API or directly to S3.  
 2. **Lambda Trigger**: Lambda processes the file when uploaded to S3.                                            
 3. **Metadata Storage**: Metadata is stored in DynamoDB.      
 4. **Monitoring**: CloudWatch logs all actions.               
                                                               
 Setup:                                                        
 1. Create an S3 bucket.                                       
 2. Deploy the Lambda function.                                
 3. Set up DynamoDB table for metadata.                        
 4. Configure API Gateway for file upload.                     
 5. Enable CloudWatch for monitoring.                          
                                                               
 Prerequisites:                                                
 - AWS Account         