from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder
import json, os
from datetime import timedelta

from models import Note
from auth import authenticate_user, create_access_token, get_current_user

app = FastAPI()

NOTES_FILE = "notes.json"

# Ensure file exists
if not os.path.exists(NOTES_FILE):
    with open(NOTES_FILE, "w") as f:
        json.dump({}, f)


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=timedelta(minutes=30)
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/notes/")
def add_note(note: Note, current_user: dict = Depends(get_current_user)):
    username = current_user["username"]

    try:
        with open(NOTES_FILE, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    if username not in data:
        data[username] = []

    note_dict = jsonable_encoder(note)
    data[username].append(note_dict)

    with open(NOTES_FILE, "w") as f:
        json.dump(data, f, indent=2)

    return {"msg": "Note added", "note": note_dict}


@app.get("/notes/")
def get_notes(current_user: dict = Depends(get_current_user)):
    username = current_user["username"]

    try:
        with open(NOTES_FILE, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    return data.get(username, [])
