import sys
import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.database import insert_vulnerability

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Headless mode from .env
HEADLESS_MODE = os.getenv("HEADLESS_MODE", "True").lower() == "true"

# Dell Security Advisories URL
DELL_SECURITY_URL = "https://www.dell.com/support/security/en-us"

def scrape_dell_vulnerabilities():
    """Scrape Dell's security advisories using Selenium"""
    options = Options()
    options.headless = HEADLESS_MODE  # Run headless if enabled
    options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass bot detection

    # Setup WebDriver for Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    logging.info("🚀 Opening Dell security page with Chrome...")
    driver.get(DELL_SECURITY_URL)
    time.sleep(5)  # Wait for JavaScript to load the page

    vulnerabilities = []

    # Find all advisory entries (Modify this selector if needed)
    advisory_entries = driver.find_elements(By.CLASS_NAME, "sc-fzqBkg")
    if not advisory_entries:
        logging.error("❌ No advisories found. The page structure may have changed.")
        driver.quit()
        return

    for advisory in advisory_entries:
        try:
            cve_id = advisory.find_element(By.TAG_NAME, "a").text.strip()
        except Exception:
            cve_id = "Unknown"

        try:
            description = advisory.find_element(By.TAG_NAME, "p").text.strip()
        except Exception:
            description = "No Description"

        try:
            published_date = advisory.find_element(By.CLASS_NAME, "sc-published-date").text.strip()
        except Exception:
            published_date = "N/A"

        severity = "High" if "critical" in description.lower() else "Medium"

        vuln_data = {
            "cve_id": cve_id,
            "description": description,
            "cvss_score": "N/A",
            "severity": severity,
            "oem": "Dell",
            "published_date": published_date,
            "source": "Dell Security Page"
        }

        vulnerabilities.append(vuln_data)
        insert_vulnerability(vuln_data)  # Store in MongoDB

    logging.info(f"✅ {len(vulnerabilities)} Dell vulnerabilities scraped & stored.")

    driver.quit()

# Run script
if __name__ == "__main__":
    scrape_dell_vulnerabilities()