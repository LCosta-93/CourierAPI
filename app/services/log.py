import os
import sys
from app.config import LOG_PATH

def log_email(recipient, subject, msg_id):
    log_entry = f"To: {recipient} | Subject: {subject} | Message-ID: {msg_id}\n"
    try:
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(log_entry)
    except Exception as e:
        print(f"[LOG ERROR] {e}", file=sys.stderr)
