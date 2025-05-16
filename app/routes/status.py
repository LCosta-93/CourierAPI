from flask import Blueprint, jsonify
from app.config import ENV, PORT, LOG_PATH, TOKEN_PATH, CREDENTIALS_PATH, VERSION

status_bp = Blueprint("status", __name__)

@status_bp.route("/status")
def status():
    return jsonify({
        "status": "ok",
        "version": VERSION,
        "env": ENV,
        "port": PORT,
        "log_path": LOG_PATH,
        "credentials_path": CREDENTIALS_PATH,
        "token_path": TOKEN_PATH
    })
