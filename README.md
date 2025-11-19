# 🌐 Cloud-Based Language Translation Service  
A fully serverless cloud application built using **AWS Lambda**, **API Gateway**, and **S3**.  
This system translates English text into multiple languages using a free translation API.

---

## 📌 Features  
✔ Translate English text into multiple languages  
✔ Fully serverless backend using AWS Lambda  
✔ Frontend hosted on AWS S3  
✔ API Gateway for secure communication  
✔ Clean UI (HTML, CSS, JavaScript)  
✔ No AWS billing (uses free external translation API)

---

## 🏗 Architecture  

```
User (Browser)
     ↓
AWS S3 (Static Website Hosting)
     ↓
API Gateway
     ↓
AWS Lambda (Python)
     ↓
Free Translation API (MyMemory)
     ↓
Response Back to User
```

---

## 🗂 Project Structure  

```
cloud-language-translation-service/
│
├── backend/
│   ├── lambda_function.py
│   ├── requirements.txt
│   └── README_BACKEND.md
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── architecture/
│   └── architecture_diagram.txt
│
├── LICENSE
└── README.md
```

---

## 🚀 How It Works  
1. User enters English text  
2. Frontend sends request → API Gateway  
3. API Gateway triggers AWS Lambda  
4. Lambda calls **MyMemory Translation API**  
5. Translated text is returned to the frontend  

---

## 🔧 Tech Stack  

### **Frontend**  
- HTML  
- CSS  
- JavaScript  

### **Backend**  
- Python  
- AWS Lambda  
- AWS API Gateway  

### **Hosting**  
- AWS S3  

---

## 🛠 Deployment Steps

### 1️⃣ Create Lambda  
- Upload `lambda_function.py`  
- Add Requests layer  
- Save  

### 2️⃣ Create API Gateway  
- Connect Lambda  
- Enable CORS  
- Deploy  
- Copy Invoke URL  

### 3️⃣ Update script.js  
Replace this line:

```javascript
const API_URL = "YOUR_API_URL_HERE";
```

with your real API link.

### 4️⃣ Host Frontend on S3  
- Enable Static Hosting  
- Upload:  
  - index.html  
  - script.js  
  - style.css  
- Open website URL  

---

## 🎯 Example Output  
**Input:** Hello  
**Output (Hindi):** नमस्ते

---

## 👩‍💻 Author  
**Prerna Tyagi**  
Cloud Computing Project – 2025

---

## 📄 License  
MIT License
