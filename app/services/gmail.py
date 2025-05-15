import os
import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from app.config import TOKEN_PATH, CREDENTIALS_PATH

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def load_token():
    if os.path.exists(TOKEN_PATH):
        return Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    # Inicia o fluxo OAuth no navegador
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
    creds = flow.run_local_server(port=0)

    # Salva token gerado
    with open(TOKEN_PATH, "w") as f:
        f.write(creds.to_json())

    return creds

def build_message(recipient, subject, body):
    message = MIMEText(body, _charset="utf-8")
    message['to'] = recipient
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

def send_email(recipient, subject, body):
    try:
        creds = load_token()
        service = build('gmail', 'v1', credentials=creds)
        message = build_message(recipient, subject, body)
        result = service.users().messages().send(userId='me', body=message).execute()
        return result['id']
    except HttpError as e:
        raise RuntimeError(f"Gmail API error: {e.status_code} {e.reason}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error: {str(e)}")
