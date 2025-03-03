from flask import Flask, jsonify, request
import logging
from database.database import get_all_vulnerabilities_ms, get_vulnerability_by_cve_ms

# Initialize Flask app
app = Flask(__name__)

# Configure Logging
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.route("/vulnerabilities", methods=["GET"])
def get_vulnerabilities():
    """Fetch all vulnerabilities or filter by severity from Microsoft."""
    severity = request.args.get("severity")  # Optional filter
    logging.info(f"📌 GET /vulnerabilities - Filter: {severity}")
    
    vulnerabilities = get_all_vulnerabilities_ms(severity)
    return jsonify(vulnerabilities), 200

@app.route("/vulnerabilities/<string:cve_id>", methods=["GET"])
def get_vulnerability(cve_id):
    """Fetch details of a specific vulnerability by CVE ID from Microsoft."""
    logging.info(f"📌 GET /vulnerabilities/{cve_id}")
    
    vulnerability = get_vulnerability_by_cve_ms(cve_id)
    if vulnerability:
        return jsonify(vulnerability), 200
    return jsonify({"error": "Vulnerability not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)  # 🚀 Debug=False for production
