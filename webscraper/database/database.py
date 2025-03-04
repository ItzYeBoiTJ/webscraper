from pymongo import MongoClient
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load MongoDB connection from environment variables
MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb+srv://admin:admin@cluster0.zhqcj.mongodb.net/"
)
DB_NAME = "oem_vulnerabilities"

# Initialize MongoDB client
try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)  # 5s timeout
    db = client[DB_NAME]

    # Test the connection
    client.server_info()  # Will raise an exception if connection fails
    logging.info("✅ Connected to MongoDB successfully!")

except Exception as e:
    logging.error(f"❌ MongoDB Connection Failed: {e}")


def insert_vulnerability(vuln_data, collection_name):
    """Insert a new vulnerability into the specified collection if it doesn't exist."""
    if not vuln_data.get("cve_id"):
        logging.warning(f"⚠️ Skipping entry with missing CVE ID: {vuln_data}")
        return

    collection = db[collection_name]  # Select collection dynamically
    if not check_existing_vulnerability(vuln_data["cve_id"], collection_name):  # Avoid duplicates
        collection.insert_one(vuln_data)
        logging.info(f"✅ Inserted {vuln_data['cve_id']} into {collection_name}.")
    else:
        logging.warning(f"⚠️ Skipping duplicate {vuln_data['cve_id']} in {collection_name}.")


def check_existing_vulnerability(cve_id, collection_name):
    """Check if a vulnerability already exists in the specified collection."""
    if not cve_id:
        return False  # Prevent checking with an empty ID
    collection = db[collection_name]
    return collection.find_one({"cve_id": cve_id}) is not None


def get_all_vulnerabilities(collection_name):
    """Retrieve all vulnerabilities from the specified collection."""
    collection = db[collection_name]
    return list(collection.find({}, {"_id": 0}))  # Excludes MongoDB _id field


def get_vulnerability_by_cve(cve_id, collection_name):
    """Retrieve a vulnerability by CVE ID from the specified collection."""
    if not cve_id:
        return None
    collection = db[collection_name]
    return collection.find_one({"cve_id": cve_id}, {"_id": 0})