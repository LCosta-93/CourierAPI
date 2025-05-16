from flask import Flask
from app.routes.email import email_bp
from app.routes.docs import docs_bp
from app.routes.status import status_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(email_bp)
    app.register_blueprint(docs_bp)

    @app.route("/healthz")
    def healthz():
        return "ok", 200
    
    app.register_blueprint(status_bp)

    return app
