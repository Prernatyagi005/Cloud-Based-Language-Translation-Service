# Cloud Translation Service

# Cloud-Based Language Translation Service (Serverless Project)

This project is a fully cloud-deployed **Language Translation Web App** built using:

- **AWS S3** (Frontend Hosting)
- **AWS Lambda** (Backend Serverless)
- **AWS API Gateway** (API Endpoint)
- **Free Translation API (MyMemory)**

## Features
- Translate English text into multiple languages
- 100% serverless architecture
- No AWS billing — uses free external translation API
- Secure, fast, and scalable

## Architecture

User → S3 Website → API Gateway → Lambda → Free Translation API → Response

## Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: AWS Lambda (Python)
- Cloud: AWS API Gateway, AWS S3

## Project Structure
(Include the same folder structure)

## 🔧 Deployment Steps
### 1. Create Lambda function
- Runtime: Python 3.x
- Upload `lambda_function.py`
- Add Layer for `requests` OR zip with dependencies

### 2. Create API Gateway HTTP API
- Connect to Lambda
- Enable CORS
- Deploy
- Copy endpoint URL

### 3. Update Frontend
Replace `YOUR_API_URL` in script.js

### 4. Deploy Frontend to S3
- Bucket → Enable public access
- Upload HTML, CSS, JS
- Enable static hosting

### 5. Open Website
Use S3 website URL.

