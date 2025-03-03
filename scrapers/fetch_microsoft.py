import sys
import os
import requests
from bs4 import BeautifulSoup
import logging

# Ensure database module is accessible
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.database import insert_vulnerability

# Microsoft Security Advisories URL
MICROSOFT_ADVISORIES_URL = "https://msrc.microsoft.com/update-guide/en-us"

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def fetch_microsoft_vulnerabilities():
    """Scrape Microsoft's security advisories for new vulnerabilities (Max 100 Entries)."""
    response = requests.get(MICROSOFT_ADVISORIES_URL)

    if response.status_code != 200:
        logging.error(f"❌ Failed to fetch Microsoft advisories. Status: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    vulnerabilities = []

    # Extract vulnerability details (Modify based on actual HTML structure)
    advisory_items = soup.find_all("div", class_="advisory-item")[:100]  # ✅ Limit to 100 results

    for vuln in advisory_items:
        cve_element = vuln.find("span", class_="cve-id")
        desc_element = vuln.find("p", class_="description")
        severity_element = vuln.find("span", class_="severity")

        if not (cve_element and desc_element and severity_element):
            continue  # Skip if required data is missing

        cve_id = cve_element.text.strip()
        description = desc_element.text.strip()
        severity = severity_element.text.strip()

        vuln_data = {
            "cve_id": cve_id,
            "description": description,
            "severity": severity,
            "oem": "Microsoft",
            "source": "Microsoft Security Advisories",
        }

        insert_vulnerability(vuln_data, "microsoft_vulnerabilities")  # ✅ Store in Microsoft collection
        vulnerabilities.append(vuln_data)

    logging.info(f"✅ {len(vulnerabilities)} vulnerabilities added from Microsoft.")


if __name__ == "__main__":
    fetch_microsoft_vulnerabilities()