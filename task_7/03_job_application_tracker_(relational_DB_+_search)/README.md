Task 3: Job Application Tracker (Relational DB + Search)

Goal: Build a Job Application Tracker with SQLModel.


Features:

JobApplication model: company, position, status, date_applied.

Each user can only access their own applications (auth required).

Endpoints:

POST /applications/ — add new job application.

GET /applications/ — list all.

GET /applications/search?status=pending.

Use error handling for invalid queries.

Use middleware to reject requests if User-Agent header is missing.

# 📌 Job Application Tracker API

A simple **FastAPI + SQLModel** project to track job applications.

## 🚀 Features
- User authentication (via `X-User` header for demo)
- CRUD endpoints for job applications
- Search applications by status
- Middleware rejecting requests without `User-Agent`
- JSON backup after inserts

## 📂 Project Structure
- app/
- main.py
- routers/
- models.py
- database.py
- auth.py
- backups/
- requirements.txt
- README.md

## ▶️ Running the App
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload

Then open: http://127.0.0.1:8000/docs