from flask import Blueprint, request, jsonify
from app.config import API_KEY
from app.services.gmail import send_email
from app.services.log import log_email

email_bp = Blueprint("email", __name__)

@email_bp.route("/send-email", methods=["POST"])
def send():
    auth_header = request.headers.get("Authorization", "")
    prefix = "Bearer "
    if not auth_header.startswith(prefix) or auth_header[len(prefix):] != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    recipient = data.get("recipient")
    subject = data.get("subject")
    body = data.get("body")

    if not all([recipient, subject, body]):
        return jsonify({"error": "Missing required fields"}), 400

    if not isinstance(recipient, str) or "@" not in recipient:
        return jsonify({"error": "Invalid recipient address"}), 400

    try:
        msg_id = send_email(recipient, subject, body)
        log_email(recipient, subject, msg_id)
        return jsonify({"status": "success", "message_id": msg_id})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
