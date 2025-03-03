from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import time
import logging
import subprocess

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize the scheduler
scheduler = BackgroundScheduler()

# Function to run a scraper script
def run_scraper(script_name):
    try:
        logging.info(f"🔄 Running {script_name}...")
        result = subprocess.run(["python", script_name], capture_output=True, text=True)
        
        if result.returncode == 0:
            logging.info(f"✅ {script_name} completed successfully.")
        else:
            logging.error(f"❌ {script_name} failed.\nError: {result.stderr}")
    
    except Exception as e:
        logging.error(f"🚨 Exception while running {script_name}: {e}")

# Schedule the scrapers
scheduler.add_job(run_scraper, IntervalTrigger(minutes=30), args=["scrapers/fetch_nvd.py"], id="nvd_scraper", replace_existing=True)
scheduler.add_job(run_scraper, IntervalTrigger(minutes=60), args=["scrapers/fetch_microsoft.py"], id="microsoft_scraper", replace_existing=True)
scheduler.add_job(run_scraper, IntervalTrigger(minutes=15), args=["scrapers/fetch_reddit.py"], id="reddit_scraper", replace_existing=True)

# Start the scheduler
scheduler.start()
logging.info("📅 Scheduler started. Press Ctrl+C to stop.")

# Keep script running
try:
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
    logging.info("🛑 Scheduler stopped.")