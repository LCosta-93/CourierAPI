# CourierAPI

Flask microservice to send transactional emails via Gmail API using OAuth 2.0 **Desktop flow**. It is production-ready, integrates with Custom GPTs, and enforces security through token-based authentication.

---

## ✉️ Features

* **POST /send-email** – Send emails via Gmail API
* **Bearer token auth** – API Key via `Authorization` header
* **OAuth 2.0 Desktop** – First run triggers browser auth, token is stored locally
* **/healthz** – Healthcheck
* **/docs** – Swagger UI documentation
* **/openapi.yaml** – OpenAPI schema export

---

## 🗂️ Project Structure

```
CourierAPI/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── routes/
│   │   ├── email.py
│   │   ├── docs.py
│   │   └── openapi.yaml
│   └── services/
│       ├── gmail.py
│       └── log.py
├── wsgi.py
├── requirements.txt
├── .env.example
├── render.yaml
```

---

## ⚙️ Setup

### 1. Install

```bash
python -m venv venv
source venv/bin/activate       # or venv\Scripts\Activate.ps1 (Windows)
pip install -r requirements.txt
cp .env.example .env           # then edit with your API_KEY
```

### 2. Add credentials

* Place your **Desktop OAuth credentials** in `credentials.json`
* Run once locally to trigger OAuth and create `token.json`

```bash
python main.py
```

---

## ▶️ Run

### Local (development)

```bash
python main.py
```

### Production (Render / Gunicorn)

```bash
gunicorn wsgi:app
```

---

## 🔐 .env.example

```env
API_KEY=your-api-key
PORT=5000
ENV=development
CREDENTIALS_PATH=credentials.json
TOKEN_PATH=token.json
LOG_PATH=email_log.txt
```

---

## 📡 API Reference

### POST `/send-email`

**Headers:**

```
Authorization: Bearer <API_KEY>
Content-Type: application/json
```

**Body:**

```json
{
  "recipient": "user@example.com",
  "subject": "Test Subject",
  "body": "This is the email body"
}
```

**Response:**

```json
{
  "status": "success",
  "message_id": "18cf1d0c8c6f3b23"
}
```

---

## 🧾 Swagger UI

* Visit `/docs` to open Swagger UI
* `/openapi.yaml` serves the schema

---

## 🚀 Deployment Guidelines

1. Run `main.py` locally once to generate `token.json`
2. Upload `token.json` and `credentials.json` to the server
3. Define the following env vars in Render:

```
API_KEY, TOKEN_PATH, CREDENTIALS_PATH, LOG_PATH
```

4. Add this to `.gitignore`:

```
.env
token.json
credentials.json
email_log.txt
main.py
```

---

## 🛡️ Security Notes

* Token-based access only; no session or cookies
* `.env` and tokens never committed
* OAuth Desktop flow avoids public redirect\_uri exposure

---

## 🤖 GPT Integration

Use this payload in a Custom GPT tool:

```http
POST https://<your-app>.onrender.com/send-email
Authorization: Bearer <API_KEY>
Content-Type: application/json

{
  "recipient": "someone@example.com",
  "subject": "Hello",
  "body": "Automated email from GPT"
}
```

---

## 🧹 Removed Components

* ❌ Session-based Flask logic (`secret_key`)
* ❌ OAuth Web flow (`auth/`, `oauthweb.py`)
* ❌ Redirect URIs

---

## 📝 License

MIT

**Author**: LCosta-93 — [github.com/LCosta-93](https://github.com/LCosta-93)

---