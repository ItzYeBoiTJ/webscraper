from pymongo import MongoClient
import os

# Load MongoDB connection from environment variables
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = "vulnerability_db"
COLLECTION_NAME = "vulnerabilities"

# Initialize MongoDB client
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

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

def get_all_vulnerabilities_ms(severity=None):
    # Fetch Microsoft vulnerabilities from your database
    # Example placeholder:
    return [{"cve_id": "CVE-2025-0001", "severity": "Critical", "description": "Example vulnerability from Microsoft"}]

def get_vulnerability_by_cve_ms(cve_id):
    # Fetch a specific Microsoft vulnerability from your database
    # Example placeholder:
    return {"cve_id": cve_id, "severity": "High", "description": "Detailed Microsoft vulnerability info"}
