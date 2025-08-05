from fastapi import FastAPI, HTTPException, Query
from models import JobApplication
from file_handler import load_applications, save_applications

app = FastAPI()

@app.post("/applications/", response_model=JobApplication)
def add_application(app_data: JobApplication):
    try:
        apps = load_applications()
        apps.append(app_data)
        save_applications(apps)
        return app_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/applications/", response_model=list[JobApplication])
def list_applications():
    try:
        return load_applications()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/applications/search", response_model=list[JobApplication])
def search_applications(status: str = Query(...)):
    try:
        apps = load_applications()
        results = [app for app in apps if app.status.lower() == status.lower()]
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
