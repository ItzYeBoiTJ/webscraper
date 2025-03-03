import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.database import insert_vulnerability

# scrapers/fetch_microsoft.py
import os
import sys
import requests
from bs4 import BeautifulSoup
import logging
<<<<<<< HEAD
from database.database import insert_vulnerability


=======
>>>>>>> 2ced185d221c8ea869bb3dfb511f523c4bbdabea
MICROSOFT_ADVISORIES_URL = "https://msrc.microsoft.com/update-guide/en-us"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def fetch_microsoft_vulnerabilities():
    """Scrape Microsoft's security advisories for new vulnerabilities."""
    response = requests.get(MICROSOFT_ADVISORIES_URL)
    
    if response.status_code != 200:
        logging.error(f"❌ Failed to fetch Microsoft advisories. Status: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    vulnerabilities = []

    # Extract vulnerability details (Example: Adjust for real Microsoft structure)
    for vuln in soup.find_all("div", class_="advisory-item"):
        cve_id = vuln.find("span", class_="cve-id").text.strip()
        description = vuln.find("p", class_="description").text.strip()
        severity = vuln.find("span", class_="severity").text.strip()

        vuln_data = {
            "cve_id": cve_id,
            "description": description,
            "severity": severity,
            "oem": "Microsoft",
            "source": "Microsoft Security Advisories"
        }

        insert_vulnerability(vuln_data)
        vulnerabilities.append(vuln_data)

    logging.info(f"✅ {len(vulnerabilities)} vulnerabilities added from Microsoft.")

if __name__ == "__main__":
    fetch_microsoft_vulnerabilities()