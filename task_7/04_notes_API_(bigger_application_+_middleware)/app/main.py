from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from .models import SQLModel
from .routers import notes

app = FastAPI(title="Notes API")

# Create DB tables
SQLModel.metadata.create_all(engine)

# CORS Settings
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:5500"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware: Count requests
request_count = 0

@app.middleware("http")
async def count_requests(request: Request, call_next):
    global request_count
    request_count += 1
    print(f"📌 Total requests so far: {request_count}")
    response = await call_next(request)
    response.headers["X-Request-Count"] = str(request_count)
    return response

# Routers
app.include_router(notes.router)

# Root
@app.get("/")
def root():
    return {"message": "Welcome to Notes API", "total_requests": request_count}
