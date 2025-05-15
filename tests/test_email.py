import os
import requests

def test_send_email_endpoint():
    api_key = os.getenv("API_KEY", "123")
    url = "http://localhost:5000/send-email"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "recipient": "example@domain.com",
        "subject": "Pytest Test",
        "body": "Message sent via test."
    }

    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 200
    assert "message_id" in response.json()
