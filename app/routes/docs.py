import os
from flask import Blueprint, send_file, render_template_string

docs_bp = Blueprint("docs", __name__)

SWAGGER_UI_HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>CourierAPI Docs</title>
  <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist/swagger-ui.css" />
</head>
<body>
  <div id="swagger-ui"></div>
  <script src="https://unpkg.com/swagger-ui-dist/swagger-ui-bundle.js"></script>
  <script>
    const ui = SwaggerUIBundle({ url: "/openapi.yaml", dom_id: "#swagger-ui" });
  </script>
</body>
</html>
"""

@docs_bp.route("/docs")
def docs():
    return render_template_string(SWAGGER_UI_HTML)

@docs_bp.route("/openapi.yaml")
def openapi():
    return send_file(os.path.join(os.path.dirname(__file__), "openapi.yaml"))
