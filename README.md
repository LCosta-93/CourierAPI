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
* **/status** – Build and environment diagnostic endpoint

---

## 📂 Project Structure

```
CourierAPI/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── email.py
│   │   ├── docs.py
│   │   ├── status.py
│   │   └── openapi.yaml
│   ├── services/
│   │   ├── __init__.py
│   │   ├── gmail.py
│   │   └── log.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── keygen.py
│   │   └── gen_token.py
│   └── templates/
│       └── swagger_ui.html
├── tests/
│   ├── __init__.py
│   ├── test_email.py
│   └── test_gmail.py
├── main.py
├── wsgi.py
├── requirements.txt
├── .env.example
├── .render.yaml
├── .gitignore
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
* Run the token generation script to initiate OAuth and create `token.json`

```bash
python -m app.utils.gen_token
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

## 📱 API Reference

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

### GET `/status`

Returns current environment configuration.

**Response:**

```json
{
  "status": "ok",
  "version": "1.0.0",
  "env": "development",
  "port": 5000,
  "log_path": "email_log.txt",
  "credentials_path": "credentials.json",
  "token_path": "token.json"
}
```

---

## 💾 Swagger UI

* Visit [`/docs`](http://localhost:5000/docs) to open Swagger UI
* `/openapi.yaml` serves the schema definition
* Template located at `app/templates/swagger_ui.html`

---

## 🚀 Deployment Guidelines

1. Run `app/utils/gen_token.py` locally once to generate `token.json`
2. Upload `token.json` and `credentials.json` to the server
3. Define the following environment variables on Render:

   ```
   API_KEY, TOKEN_PATH, CREDENTIALS_PATH, LOG_PATH, PORT, ENV
   ```
4. Ensure these files are in `.gitignore`:

   ```
   .env
   credentials.json
   token.json
   email_log.txt
   ```

---

## 🧱 Deployment-Grade Features

✅ High Priority
- Add Docker support with Dockerfile
- Enable CORS for frontend integration

🧩 Technical Priority
- Expose BUILD_HASH for tracking CI deployments
- Automate OpenAPI regeneration

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

## 📝 License

MIT

---

**Author**: LCosta-93 — [github.com/LCosta-93](https://github.com/LCosta-93)
