VERSION = "1.0.0"

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise RuntimeError("API_KEY is required in .env")

PORT = int(os.getenv("PORT", 5000))

TOKEN_PATH = os.getenv("TOKEN_PATH", "token.json")
CREDENTIALS_PATH = os.getenv("CREDENTIALS_PATH", "credentials.json")
LOG_PATH = os.getenv("LOG_PATH", "email_log.txt")

# Optional: for logs or diagnostics
ENV = os.getenv("ENV", "development")
