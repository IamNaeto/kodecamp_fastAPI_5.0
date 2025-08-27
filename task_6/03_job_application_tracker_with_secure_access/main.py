from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder
import json, os
from models import JobApplication
from auth import authenticate_user, create_access_token, get_current_user

app = FastAPI()

APPLICATIONS_FILE = "applications.json"

# Ensure file exists
if not os.path.exists(APPLICATIONS_FILE):
    with open(APPLICATIONS_FILE, "w") as f:
        json.dump({}, f)   # store per-user apps in dict: { "alice": [...], "bob": [...] }


@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid credentials"
        )
    token = create_access_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}


@app.post("/applications/")
def add_application(
    application: JobApplication, 
    current_user: dict = Depends(get_current_user)   # current_user is dict
):
    username = current_user["username"]              # extract username string

    try:
        with open(APPLICATIONS_FILE, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    if username not in data:
        data[username] = []

    # Convert Pydantic model into JSON-serializable dict
    app_dict = jsonable_encoder(application)

    data[username].append(app_dict)

    with open(APPLICATIONS_FILE, "w") as f:
        json.dump(data, f, indent=2)

    return {"msg": "Application added", "application": app_dict}


@app.get("/applications/")
def get_applications(current_user: dict = Depends(get_current_user)):
    username = current_user["username"]

    try:
        with open(APPLICATIONS_FILE, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    return data.get(username, [])
