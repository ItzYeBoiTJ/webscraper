# 🚀 OEM Vulnerability Tracker

## 📌 Overview
OEM Vulnerability Tracker is a **real-time vulnerability monitoring system** that collects, stores, and tracks **critical vulnerabilities** from the **National Vulnerability Database (NVD)** and **OEM (Original Equipment Manufacturer) security bulletins** (e.g., Intel, NVIDIA). The system:

✅ **Scrapes vulnerabilities from NVD & OEM websites**
✅ **Stores data in MongoDB**
✅ **Serves vulnerabilities via a Flask API**
✅ **Automatically sends email alerts for critical vulnerabilities**

---

## 📂 Project Structure
```
📁 oem-vuln-tracker/
├── 📂 backend/  
│   ├── 📜 fetch_nvd.py  # Fetches vulnerabilities from NVD API  
│   ├── 📜 scrape_oem.py  # Scrapes vulnerabilities from OEM websites  
│   ├── 📜 send_email.py  # Sends email alerts for critical vulnerabilities  
│   ├── 📜 db.py  # MongoDB database operations  
│   ├── 📜 api.py  # Flask API to serve vulnerability data  
│   ├── 📜 config.py  # Configuration settings  
├── 📂 frontend/ (To be built later)  
│   ├── 📜 index.html  # Web UI Dashboard  
│   ├── 📜 app.js  # Handles frontend logic  
│   ├── 📜 styles.css  # UI Styling  
├── 📜 requirements.txt  # Python dependencies  
├── 📜 README.md  # Project documentation  
├── 📜 .env  # Email credentials (DO NOT SHARE)  
```

---

## ⚙️ **Installation & Setup**

### **1️⃣ Install Dependencies**
Ensure you have **Python 3.8+** installed. Then, install required libraries:
```bash
pip install -r requirements.txt
```
If `requirements.txt` is missing, manually install:
```bash
pip install flask scrapy beautifulsoup4 requests pymongo httpx
```

### **2️⃣ Set Up MongoDB**
- **Option 1:** Use **MongoDB Atlas (Cloud)** → Create a cluster at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
- **Option 2:** Use **local MongoDB** (Install [MongoDB Community Server](https://www.mongodb.com/try/download/community)).

Make sure your **MongoDB server is running** before starting the project.

### **3️⃣ Configure Email Alerts**
Create a `.env` file in the **root directory** with your email credentials:
```
EMAIL_SENDER=your-email@gmail.com  
EMAIL_PASSWORD=your-app-password  
EMAIL_RECEIVER=recipient@example.com  
```
⚠️ **Important:** If using **Gmail**, enable ["Less Secure Apps"](https://myaccount.google.com/security) or use an **App Password**.

---

## 🛠️ **How to Use?**

### **1️⃣ Fetch Vulnerabilities from NVD API**
Run the script to fetch **latest critical vulnerabilities** from NVD:
```bash
python backend/fetch_nvd.py
```
This will:
✔ Fetch latest vulnerabilities  
✔ Store them in MongoDB  
✔ Send an email if a **new critical vulnerability** is found  

### **2️⃣ Scrape OEM Security Bulletins**
To scrape **Intel/NVIDIA security bulletins**, run:
```bash
python backend/scrape_oem.py
```
This will:
✔ Extract latest vulnerabilities from OEM websites  
✔ Store them in MongoDB  

### **3️⃣ Run Flask API (Backend Server)**
Start the **Flask API** to serve vulnerabilities via HTTP:
```bash
python backend/api.py
```
Open your browser or Postman and visit:
- 🔹 `http://127.0.0.1:5000/vulnerabilities` → Get all vulnerabilities  
- 🔹 `http://127.0.0.1:5000/vulnerabilities/Intel` → Get Intel-specific vulnerabilities  
- 🔹 `http://127.0.0.1:5000/vulnerabilities/high-severity` → Get only high-risk vulnerabilities  

---

## 🚀 **Automate Data Fetching (Optional)**
To fetch vulnerabilities **automatically every 6 hours**, schedule a task:

### **Linux/Mac - Use `cron`**
```bash
crontab -e
```
Add the following line:
```
0 */6 * * * /usr/bin/python3 /path-to-project/backend/fetch_nvd.py
```

### **Windows - Use Task Scheduler**
1. Open **Task Scheduler** → **Create Basic Task**  
2. Set **Trigger** → Run every **6 hours**  
3. Set **Action** → Run `python fetch_nvd.py`  

---

## 🛠️ **Future Improvements**
✔ Add a **frontend dashboard** to visualize vulnerabilities  
✔ Improve **filtering & ranking** of vulnerabilities  
✔ Add support for **more OEM security sources**  

---

