# fetch_mitre.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import requests
from bs4 import BeautifulSoup
import logging
from database.database import insert_vulnerability

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# MITRE CVE List URL
MITRE_CVE_URL = "https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=windows"

def fetch_mitre_vulnerabilities():
    """Scrape vulnerability data from MITRE CVE List (Max 100 Entries)"""
    response = requests.get(MITRE_CVE_URL)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        vulnerabilities = []

        # Find all CVE entries in the table (Limit to 100)
        rows = soup.select("table tr")[1:101]  # Skip header row, limit to 100 entries

        for row in rows:
            cols = row.find_all("td")
            if len(cols) < 2:
                continue
            
            cve_id = cols[0].text.strip()
            description = cols[1].text.strip()
            severity = "Unknown"  # MITRE does not provide severity

            vuln_data = {
                "cve_id": cve_id,
                "description": description,
                "cvss_score": "N/A",
                "severity": severity,
                "oem": "MITRE",
                "published_date": "N/A",
                "source": "MITRE CVE List"
            }

            insert_vulnerability(vuln_data)
            vulnerabilities.append(vuln_data)

        logging.info(f"✅ {len(vulnerabilities)} vulnerabilities fetched from MITRE and stored.")
    else:
        logging.error(f"❌ Failed to fetch MITRE data. Status Code: {response.status_code}")

if __name__ == "__main__":
    fetch_mitre_vulnerabilities()
