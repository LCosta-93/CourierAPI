# app/utils/gen_token.py

from app.config import CREDENTIALS_PATH, TOKEN_PATH
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
import os

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def generate_token():
    if os.path.exists(TOKEN_PATH):
        print(f"Token já existe em: {TOKEN_PATH}")
        return

    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
    creds = flow.run_local_server(port=0)

    with open(TOKEN_PATH, 'w') as token_file:
        token_file.write(creds.to_json())

    print(f"Token salvo em: {TOKEN_PATH}")

if __name__ == "__main__":
    generate_token()
