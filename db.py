# db.py
from pymongo import MongoClient
import config

# Connect to MongoDB
client = MongoClient(config.MONGO_URI)
db = client[config.DB_NAME]
collection = db[config.COLLECTION_NAME]

def insert_vulnerability(data):
    """Insert vulnerability data into MongoDB"""
    collection.insert_one(data)

def get_all_vulnerabilities():
    """Retrieve all vulnerabilities"""
    return list(collection.find({}, {"_id": 0}))  # Hide MongoDB's default _id

def get_vulnerabilities_by_oem(oem_name):
    """Retrieve vulnerabilities for a specific OEM"""
    return list(collection.find({"oem": oem_name}, {"_id": 0}))
