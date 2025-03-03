# test_db.py
from db import insert_vulnerability, get_all_vulnerabilities

# Sample data
sample_vuln = {
    "cve_id": "CVE-2024-0001",
    "description": "Test vulnerability affecting Intel CPUs.",
    "cvss_score": 9.8,
    "severity": "High",
    "oem": "Intel",
    "published_date": "2024-03-02",
    "source": "Test Data"
}

# Insert test data
insert_vulnerability(sample_vuln)

# Fetch all vulnerabilities
vulns = get_all_vulnerabilities()
print(vulns)
