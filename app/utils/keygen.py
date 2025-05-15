import secrets

def generate_flask_secret_key(length=64):
    return secrets.token_urlsafe(length)

if __name__ == "__main__":
    key = generate_flask_secret_key()
    print("FLASK_SECRET_KEY=" + key)
