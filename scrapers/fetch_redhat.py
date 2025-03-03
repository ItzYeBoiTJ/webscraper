# fetch_redhat.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import requests
import xml.etree.ElementTree as ET
import logging
from database.database import insert_vulnerability

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Red Hat Security Advisories RSS Feed
REDHAT_RSS_URL = "https://access.redhat.com/security/data/metrics/cve.xml"

def fetch_redhat_vulnerabilities():
    """Fetch vulnerability data from Red Hat Security Advisories"""
    response = requests.get(REDHAT_RSS_URL)

    if response.status_code == 200:
        root = ET.fromstring(response.content)
        vulnerabilities = []

        for item in root.findall(".//entry"):
            cve_id = item.find("id").text.strip()
            description = item.find("summary").text.strip() if item.find("summary") is not None else "No description available"
            severity = item.find("severity").text.strip() if item.find("severity") is not None else "Unknown"

            vuln_data = {
                "cve_id": cve_id,
                "description": description,
                "cvss_score": "N/A",
                "severity": severity,
                "oem": "Red Hat",
                "published_date": "N/A",
                "source": "Red Hat Security Advisories"
            }

            insert_vulnerability(vuln_data)
            vulnerabilities.append(vuln_data)

        logging.info(f"✅ {len(vulnerabilities)} vulnerabilities fetched from Red Hat and stored.")
    else:
        logging.error(f"❌ Failed to fetch Red Hat data. Status Code: {response.status_code}")

if __name__ == "__main__":
    fetch_redhat_vulnerabilities()