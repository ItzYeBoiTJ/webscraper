import sys
import os
import asyncio
import httpx
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.database import insert_vulnerability, check_existing_vulnerability

# NVD API URL
NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


async def fetch_nvd_page(start_index):
    """Fetch a single page of vulnerabilities from the NVD API."""
    async with httpx.AsyncClient() as client:
        params = {
            "startIndex": start_index,
            "resultsPerPage": 100,  # Only fetch 100 results total
            "cvssV3Severity": "CRITICAL"
        }
        try:
            response = await client.get(NVD_API_URL, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            logging.error(f"❌ API Error: {e.response.status_code} - {e.response.text}")
        except httpx.RequestError as e:
            logging.error(f"❌ Request Error: {e}")
        return None


async def fetch_all_nvd_vulnerabilities():
    """Fetch only 100 vulnerabilities (limited for performance)."""
    vulnerabilities = []

    # Fetch a single batch of 100 results
    data = await fetch_nvd_page(0)

    if not data:
        logging.error("❌ Failed to fetch vulnerabilities from NVD.")
        return

    for item in data.get("vulnerabilities", []):
        cve_info = item.get("cve", {})

        vuln_data = {
            "cve_id": cve_info.get("id", "Unknown"),
            "description": cve_info.get("descriptions", [{}])[0].get("value", "No description"),
            "cvss_score": cve_info.get("metrics", {}).get("cvssMetricV31", [{}])[0].get("cvssData", {}).get("baseScore", "N/A"),
            "severity": cve_info.get("metrics", {}).get("cvssMetricV31", [{}])[0].get("cvssData", {}).get("baseSeverity", "N/A"),
            "oem": extract_vendor_name(cve_info),
            "published_date": cve_info.get("published", "N/A"),
            "source": "NVD API"
        }

        if not check_existing_vulnerability(vuln_data["cve_id"]):
            vulnerabilities.append(vuln_data)
            insert_vulnerability(vuln_data)

    logging.info(f"✅ {len(vulnerabilities)} new vulnerabilities added from NVD.")


def extract_vendor_name(cve_info):
    """Extract vendor name from NVD JSON safely."""
    try:
        configurations = cve_info.get("configurations", [])

        if isinstance(configurations, list):
            for config in configurations:
                if isinstance(config, dict) and "nodes" in config:
                    nodes = config["nodes"]
                    if isinstance(nodes, list):
                        for node in nodes:
                            if isinstance(node, dict) and "cpeMatch" in node:
                                cpe_match = node["cpeMatch"]
                                if isinstance(cpe_match, list):
                                    for cpe in cpe_match:
                                        if isinstance(cpe, dict) and "criteria" in cpe:
                                            return cpe["criteria"].split(":")[3]  # Extract vendor name

        elif isinstance(configurations, dict):
            nodes = configurations.get("nodes", [])
            if isinstance(nodes, list) and nodes:
                cpe_matches = nodes[0].get("cpeMatch", [])
                if isinstance(cpe_matches, list) and cpe_matches:
                    return cpe_matches[0].get("criteria", "Unknown").split(":")[3]

        return "Unknown"
    except (KeyError, IndexError, TypeError):
        return "Unknown"


if __name__ == "__main__":
    asyncio.run(fetch_all_nvd_vulnerabilities())