from app import create_app
from app.config import PORT

print("[INFO] Inicializando app Flask...")

app = create_app()

if __name__ == "__main__":
    print(f"[INFO] Executando em http://localhost:{PORT}")
    app.run(debug=True, port=PORT)
