import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Load email credentials from environment variables
EMAIL_SENDER = os.getenv("EMAIL_SENDER", "your_email@example.com")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "your_email_password")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER", "recipient@example.com")

SMTP_SERVER = "smtp.gmail.com"  # Change if using Outlook/Yahoo
SMTP_PORT = 465  # SSL Port

def send_email_alert(vulnerability):
    """Send an email alert for a new critical vulnerability."""
    subject = f"🚨 Critical Vulnerability Alert: {vulnerability['cve_id']}"
    body = (
        f"🔴 **New Critical Vulnerability Detected!**\n\n"
        f"**CVE ID:** {vulnerability['cve_id']}\n"
        f"**Severity:** {vulnerability['severity']}\n"
        f"**Score:** {vulnerability['cvss_score']}\n"
        f"**Description:** {vulnerability['description']}\n"
        f"**Published Date:** {vulnerability['published_date']}\n"
        f"**Source:** {vulnerability['source']}\n\n"
        f"Please take immediate action! 🔐"
    )

    # Create Email Message
    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        print(f"✅ Email alert sent for {vulnerability['cve_id']}")
    except Exception as e:
        print(f"❌ Email sending failed: {e}")