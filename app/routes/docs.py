import os
from flask import Blueprint, send_file, render_template

docs_bp = Blueprint("docs", __name__, template_folder="templates")

@docs_bp.route("/docs")
def docs():
    return render_template("swagger_ui.html")

@docs_bp.route("/openapi.yaml")
def openapi():
    return send_file(os.path.join(os.path.dirname(__file__), "openapi.yaml"))
