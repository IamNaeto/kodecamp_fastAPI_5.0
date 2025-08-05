import os
from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import PlainTextResponse

app = FastAPI()
NOTES_DIR = "notes"

# Create the directory if it doesn't exist
os.makedirs(NOTES_DIR, exist_ok=True)

# Utility function
def get_note_path(title: str) -> str:
    return os.path.join(NOTES_DIR, f"{title}.txt")

@app.post("/notes/")
def create_note(title: str = Body(...), content: str = Body(...)):
    try:
        path = get_note_path(title)
        if os.path.exists(path):
            raise HTTPException(status_code=400, detail="Note already exists.")
        with open(path, "w") as f:
            f.write(content)
        return {"message": f"Note '{title}' created successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/notes/{title}", response_class=PlainTextResponse)
def read_note(title: str):
    try:
        path = get_note_path(title)
        if not os.path.exists(path):
            raise HTTPException(status_code=404, detail="Note not found.")
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/notes/{title}")
def update_note(title: str, content: str = Body(...)):
    try:
        path = get_note_path(title)
        if not os.path.exists(path):
            raise HTTPException(status_code=404, detail="Note not found.")
        with open(path, "w") as f:
            f.write(content)
        return {"message": f"Note '{title}' updated successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/notes/{title}")
def delete_note(title: str):
    try:
        path = get_note_path(title)
        if not os.path.exists(path):
            raise HTTPException(status_code=404, detail="Note not found.")
        os.remove(path)
        return {"message": f"Note '{title}' deleted successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
