
# Secure Student Portal API

FastAPI project where students can register, log in, and view their grades. 
Supports **HTTP Basic** and **OAuth2 (Bearer token)** on `GET /grades/`. 
Student data is stored in `students.json` with **bcrypt-hashed** passwords.

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

Open docs at http://127.0.0.1:8000/docs

## Endpoints

- `POST /register/` — JSON body: `{ "username": "alice", "password": "secret123", "grades": [85, 92, 77] }`
- `POST /login/` — OAuth2 Password flow (form fields): `username`, `password`. Returns `{ access_token, token_type }`.
- `GET /grades/` — Requires **either**:
  - HTTP Basic: set `Authorization: Basic <base64(username:password)>`, or
  - OAuth2 Bearer: set `Authorization: Bearer <access_token>`

## Example `curl`

Register:
```bash
curl -X POST http://127.0.0.1:8000/register/   -H "Content-Type: application/json"   -d '{"username":"alice","password":"secret123","grades":[88,93]}'
```

Login (OAuth2):
```bash
curl -X POST http://127.0.0.1:8000/login/   -H "Content-Type: application/x-www-form-urlencoded"   -d "username=alice&password=secret123"
```

Fetch grades (Bearer):
```bash
TOKEN="paste-token-here"
curl http://127.0.0.1:8000/grades/ -H "Authorization: Bearer $TOKEN"
```

Fetch grades (Basic):
```bash
# macOS/Linux: base64
BASIC=$(printf "alice:secret123" | base64)
curl http://127.0.0.1:8000/grades/ -H "Authorization: Basic $BASIC"
```

## Data storage

- Students are stored in `students.json` as a dictionary keyed by username:
```json
{
  "alice": {
    "password_hash": "$2b$12$...",
    "grades": [88, 93]
  }
}
```
- The API uses try/except to handle read/write errors gracefully.

## Notes

- Tokens are kept in memory for demo simplicity. In production, use a DB/redis + JWT with expiry.
- You can set `STUDENTS_FILE=/path/to/students.json` as an environment variable to move storage.
