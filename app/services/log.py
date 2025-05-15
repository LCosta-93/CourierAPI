import os
from app.config import LOG_PATH

def log_email(recipient, subject, msg_id):
    try:
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(f"To: {recipient} | Subject: {subject} | Message-ID: {msg_id}\n")
    except Exception:
        pass  # falha no log não deve interromper aplicação
