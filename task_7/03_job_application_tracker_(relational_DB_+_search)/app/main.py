from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .database import engine
from .models import SQLModel
from .routers import applications

app = FastAPI(title="Job Application Tracker")

# Create tables
SQLModel.metadata.create_all(engine)

# Middleware: Reject requests if no User-Agent
@app.middleware("http")
async def check_user_agent(request: Request, call_next):
    if "user-agent" not in request.headers:
        return JSONResponse(status_code=400, content={"detail": "User-Agent header required"})
    return await call_next(request)

# Routers
app.include_router(applications.router)
