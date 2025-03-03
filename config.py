import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# config.py
MONGO_URI = "mongodb://localhost:27017/oem_vulnerabilities"  # Change if using MongoDB Atlas
DB_NAME = "oem_vulnerabilities"
COLLECTION_NAME = "vulnerabilities"

EMAIL_SENDER = os.getenv("EMAIL_SENDER", "your_email@example.com")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "your_email_password")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER", "recipient@example.com")

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")  # Change if using Outlook/Yahoo
SMTP_PORT = int(os.getenv("SMTP_PORT", 465))  # SSL Port

# Scraper Configuration
NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
MICROSOFT_ADVISORIES_URL = "https://msrc.microsoft.com/update-guide/en-us"
REDDIT_SEARCH_QUERY = "security OR vulnerability OR exploit"

# Scheduler Configuration
SCRAPER_INTERVAL_MINUTES = 30  # Frequency for running scrapers