from pymongo import MongoClient
import os

# Load MongoDB connection from environment variables
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://admin:admin@cluster0.zhqcj.mongodb.net/")
DB_NAME = "oem_vulnerabilities"
COLLECTION_NAME = "vulnerabilities"

# Initialize MongoDB client
try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)  # 5s timeout
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    
    # Test the connection
    client.server_info()  # Will raise an exception if connection fails
    print("✅ Connected to MongoDB successfully!")

except Exception as e:
    print(f"❌ MongoDB Connection Failed: {e}")

def insert_vulnerability(vuln_data):
    """Insert a new vulnerability if it doesn't already exist."""
    if not collection.find_one({"cve_id": vuln_data["cve_id"]}):  # Avoid duplicates
        collection.insert_one(vuln_data)
        print(f"✅ Inserted: {vuln_data['cve_id']}")
    else:
        print(f"⚠️ Skipping duplicate: {vuln_data['cve_id']}")

def check_existing_vulnerability(cve_id):
    """Check if a vulnerability already exists."""
    return collection.find_one({"cve_id": cve_id}) is not None

def get_all_vulnerabilities():
    """Retrieve all vulnerabilities from MongoDB."""
    return list(collection.find({}, {"_id": 0}))  # Excludes MongoDB _id field

def get_vulnerability_by_cve(cve_id):
    """Retrieve a vulnerability by CVE ID"""
    return collection.find_one({"cve_id": cve_id}, {"_id": 0})