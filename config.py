import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://admin:admin@cluster0.zhqcj.mongodb.net/oem_vulnerabilities?retryWrites=true&w=majority")
DB_NAME = os.getenv("DB_NAME", "oem_vulnerabilities")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "vulnerabilities")

# Email Configuration
EMAIL_SENDER = os.getenv("EMAIL_SENDER", "your_email@example.com")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "your_email_password")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER", "recipient@example.com")

# SMTP Configuration
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")  # Change for Outlook/Yahoo
SMTP_PORT = int(os.getenv("SMTP_PORT", "465"))  # SSL Port

# Scraper Configuration
MITRE_CVE_URL = "https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=windows"
REDHAT_RSS_URL = "https://access.redhat.com/security/data/metrics/cve.xml"
DELL_SECURITY_URL = "https://www.dell.com/support/security/en-us"
NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
MICROSOFT_ADVISORIES_URL = "https://msrc.microsoft.com/update-guide/en-us"
REDDIT_SEARCH_QUERY = "security OR vulnerability OR exploit"

# Scheduler Configuration
SCRAPER_INTERVAL_MINUTES = int(os.getenv("SCRAPER_INTERVAL_MINUTES", "30"))  # Frequency for running scrapers   