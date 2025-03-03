# scrapers/fetch_reddit.py
import praw
import os
import logging
from database.database import insert_vulnerability

# Reddit API credentials (Replace with actual values)
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID", "your_client_id")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET", "your_client_secret")
USER_AGENT = "vuln-scraper"

# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize Reddit API client
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=USER_AGENT
)

def fetch_reddit_vulnerabilities():
    """Scrape Reddit posts for security discussions mentioning CVEs."""
    vulnerabilities = []
    subreddits = ["netsec", "sysadmin"]

    for subreddit in subreddits:
        for post in reddit.subreddit(subreddit).new(limit=50):
            if "CVE-" in post.title:  # Check if the post mentions a CVE
                vuln_data = {
                    "cve_id": post.title.split()[0],
                    "description": post.title,
                    "source": f"Reddit ({subreddit})"
                }
                insert_vulnerability(vuln_data)
                vulnerabilities.append(vuln_data)

    logging.info(f"✅ {len(vulnerabilities)} vulnerabilities added from Reddit.")

if __name__ == "__main__":
    fetch_reddit_vulnerabilities()