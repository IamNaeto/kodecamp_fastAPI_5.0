Task 4: Notes API (Bigger Application + Middleware)

Goal: Build a Notes management API with file & database storage.

Features:

Note model: title, content, created_at (SQLModel).

Endpoints:

POST /notes/ — create note.

GET /notes/ — list all.

GET /notes/{id} — view single note.

DELETE /notes/{id} — delete note.

Use middleware to count total requests made and log them.

Save a backup of all notes in notes.json

Add CORS for multiple origins (http://localhost:3000, http://127.0.0.1:5500).

# 📝 Notes API

A **FastAPI + SQLModel** Notes Management API with:
- Database + JSON backup
- Request-counting middleware
- CORS support

## 🚀 Features
- Create, list, view, and delete notes
- JSON backup after every change
- Middleware counts total requests
- CORS for `http://localhost:3000` and `http://127.0.0.1:5500`

## ▶️ Run the app
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
