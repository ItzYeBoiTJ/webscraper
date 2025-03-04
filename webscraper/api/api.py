import sys
import os
import logging
from flask import Flask, jsonify, request

# Ensure parent directory is in Python path (fixes import issues)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.database import get_all_vulnerabilities, get_vulnerability_by_cve, client, db

# Initialize Flask app
app = Flask(__name__)

# Configure Logging
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("🚀 API is starting...")

@app.route("/health", methods=["GET"])
def health_check():
    """Check MongoDB database connection health."""
    logging.info("📌 Checking database health...")
    try:
        db.command("ping")  # Lighter and safer than `client.server_info()`
        collection_name = "vulnerabilities"
        if collection_name in db.list_collection_names():
            return jsonify({"status": "Database is connected", "collection": collection_name}), 200
        else:
            return jsonify({"status": "Database connected, but collection not found"}), 404
    except Exception as e:
        logging.error(f"❌ Database connection failed: {e}")
        return jsonify({"status": "Database connection failed", "error": str(e)}), 503

@app.route("/vulnerabilities", methods=["GET"])
def get_vulnerabilities():
    """Fetch all vulnerabilities."""
    logging.info("📌 GET /vulnerabilities")
    
    vulnerabilities = get_all_vulnerabilities()
    return jsonify(vulnerabilities), 200

@app.route("/vulnerabilities/<string:cve_id>", methods=["GET"])
def get_vulnerability(cve_id):
    """Fetch details of a specific vulnerability by CVE ID."""
    logging.info(f"📌 GET /vulnerabilities/{cve_id}")
    
    vulnerability = get_vulnerability_by_cve(cve_id)
    if vulnerability:
        return jsonify(vulnerability), 200
    return jsonify({"error": "Vulnerability not found"}), 404

if __name__ == "__main__":
    logging.info("🔥 Running Flask API on http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=False)  # 🚀 Debug=False for production