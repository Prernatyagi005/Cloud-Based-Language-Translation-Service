# Cloud Translation Service

# Cloud-Based Language Translation Service  
A fully serverless cloud application built using **AWS Lambda**, **API Gateway**, and **S3**.  
The system translates English text into multiple languages using a free translation API.

---

## Features  
✔ Translate English text into multiple languages  
✔ Fully serverless backend using AWS Lambda  
✔ Frontend hosted using AWS S3  
✔ API Gateway for secure communication  
✔ Clean UI (HTML, CSS, JavaScript)  
✔ No AWS billing (uses free external translation API)

---

## Architecture  
User (Browser)
↓
AWS S3 (Static Frontend Hosting)
↓
API Gateway
↓
AWS Lambda (Python)
↓
Free Translation API (MyMemory)
↓
Response Back to User


## Project Structure  
cloud-language-translation-service/
│
├── backend/
│ ├── lambda_function.py
│ ├── requirements.txt
│ └── README_BACKEND.md
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
├── architecture/
│ └── architecture_diagram.txt
│
├── LICENSE
└── README.md

## 🚀 How It Works  
1. User enters English text and selects a target language  
2. Frontend sends request → API Gateway  
3. API Gateway triggers AWS Lambda  
4. Lambda calls **MyMemory Translation API**  
5. Translated text is returned to the frontend


## 🔧 Tech Stack  
### **Frontend:**  
- HTML  
- CSS  
- JavaScript  

### **Backend:**  
- Python  
- AWS Lambda  
- AWS API Gateway  

### **Hosting:**  
- AWS S3  

## Project Structure
(Include the same folder structure)

## Deployment Steps
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

