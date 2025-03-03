# scrapers/fetch_nvd.py
import asyncio
import httpx
import logging
from database import insert_vulnerability, check_existing_vulnerability


# NVD API URL
NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

async def fetch_nvd_page(start_index):
    """Fetch a single page of vulnerabilities from NVD API."""
    async with httpx.AsyncClient() as client:
        params = {
            "startIndex": start_index,
            "resultsPerPage": 200,  # Fetch in batches
            "cvssV3Severity": "CRITICAL"
        }
        response = await client.get(NVD_API_URL, params=params, timeout=10)
        response.raise_for_status()  
        return response.json()

async def fetch_all_nvd_vulnerabilities():
    """Fetch all vulnerabilities using pagination."""
    vulnerabilities = []
    tasks = []

    for start in range(0, 1000, 200):  # Fetch up to 1000 results
        tasks.append(fetch_nvd_page(start))

    results = await asyncio.gather(*tasks)

    for data in results:
        for item in data.get("vulnerabilities", []):
            cve_info = item["cve"]
            vuln_data = {
                "cve_id": cve_info["id"],
                "description": cve_info["descriptions"][0]["value"],
                "cvss_score": cve_info.get("metrics", {}).get("cvssMetricV31", [{}])[0].get("cvssData", {}).get("baseScore", "N/A"),
                "severity": cve_info.get("metrics", {}).get("cvssMetricV31", [{}])[0].get("cvssData", {}).get("baseSeverity", "N/A"),
                "oem": extract_vendor_name(cve_info),
                "published_date": cve_info["published"],
                "source": "NVD API"
            }
            if not check_existing_vulnerability(vuln_data["cve_id"]):
                vulnerabilities.append(vuln_data)
                insert_vulnerability(vuln_data)

    logging.info(f"✅ {len(vulnerabilities)} new vulnerabilities added from NVD.")

def extract_vendor_name(cve_info):
    """Extract vendor name from NVD JSON."""
    try:
        return cve_info["configurations"]["nodes"][0]["cpeMatch"][0]["criteria"].split(":")[3]
    except (KeyError, IndexError):
        return "Unknown"

if __name__ == "__main__":
    asyncio.run(fetch_all_nvd_vulnerabilities())
