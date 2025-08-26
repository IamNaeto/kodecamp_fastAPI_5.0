from fastapi import FastAPI
from routes import auth, grades

app = FastAPI(
    title="Secure Student Portal API",
    version="1.0.0",
    description="Students can register, log in, and view grades using HTTP Basic or OAuth2."
)

app.include_router(auth.router)
app.include_router(grades.router)

@app.get("/", tags=["root"])
def index():
    return {
        "message": "Secure Student Portal API",
        "endpoints": {
            "POST /register/": "Register a new student",
            "POST /login/": "Login (OAuth2) to get Bearer token",
            "GET /grades/": "Get grades (Auth: Basic or Bearer)"
        }
    }
