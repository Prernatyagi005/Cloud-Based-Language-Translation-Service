# 🌐 Cloud-Based Language Translation Service  
A fully serverless cloud application built using **AWS Lambda**, **API Gateway**, and **S3**.  
The system translates English text into multiple languages using a free translation API.

---

## 📌 Features  
✔ Translate English text into multiple languages  
✔ Fully serverless backend using AWS Lambda  
✔ Frontend hosted using AWS S3  
✔ API Gateway for secure communication  
✔ Clean UI (HTML, CSS, JavaScript)  
✔ No AWS billing (uses free external translation API)

---

## 🏗 Architecture  

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

yaml
Copy code

---

## 🗂 Project Structure  

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

yaml
Copy code

---

## 🚀 How It Works  
1. User enters English text and selects a target language  
2. Frontend sends request → API Gateway  
3. API Gateway triggers AWS Lambda  
4. Lambda calls **MyMemory Translation API**  
5. Translated text is returned to the frontend  

---

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

---

## 🛠 Steps to Deploy on AWS

### 1️⃣ Create Lambda Function  
- Runtime: Python 3.12  
- Upload `lambda_function.py`  
- Add **Requests library layer**  
- Save & test

### 2️⃣ Create HTTP API (API Gateway)  
- Connect Lambda integration  
- Enable CORS (Allow all origins, headers, methods)  
- Deploy API  
