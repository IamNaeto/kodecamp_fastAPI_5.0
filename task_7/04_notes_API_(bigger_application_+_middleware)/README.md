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
