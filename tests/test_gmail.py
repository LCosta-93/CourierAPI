from unittest.mock import patch
from app.services import gmail

@patch("app.services.gmail.load_token")
@patch("app.services.gmail.build")
def test_send_email_success(mock_build, mock_token):
    mock_token.return_value = "fake-creds"

    mock_service = mock_build.return_value
    mock_users = mock_service.users.return_value
    mock_messages = mock_users.messages.return_value
    mock_send = mock_messages.send.return_value
    mock_send.execute.return_value = {"id": "abc123"}

    result = gmail.send_email("test@example.com", "Test Subject", "Test Body")
    assert result == "abc123"
