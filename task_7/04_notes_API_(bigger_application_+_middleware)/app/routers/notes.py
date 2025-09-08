from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from pathlib import Path
import json

from ..database import get_session
from ..models import Note

router = APIRouter(prefix="/notes", tags=["notes"])

BACKUP_FILE = Path(__file__).resolve().parent.parent / "backups" / "notes.json"

# 🔄 Save backup to JSON
def save_backup(notes: list[Note]):
    data = []
    for note in notes:
        d = note.dict()
        d["created_at"] = d["created_at"].isoformat()  # convert datetime to string
        data.append(d)
    BACKUP_FILE.write_text(json.dumps(data, indent=4))


# ✅ Create Note
@router.post("/", response_model=Note)
def create_note(note: Note, session: Session = Depends(get_session)):
    session.add(note)
    session.commit()
    session.refresh(note)

    notes = session.exec(select(Note)).all()
    save_backup(notes)
    return note

# ✅ List Notes
@router.get("/", response_model=List[Note])
def list_notes(session: Session = Depends(get_session)):
    notes = session.exec(select(Note)).all()
    return notes

# ✅ Get Single Note
@router.get("/{note_id}", response_model=Note)
def get_note(note_id: int, session: Session = Depends(get_session)):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

# ✅ Delete Note
@router.delete("/{note_id}")
def delete_note(note_id: int, session: Session = Depends(get_session)):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    session.delete(note)
    session.commit()

    notes = session.exec(select(Note)).all()
    save_backup(notes)

    return {"detail": f"Note {note_id} deleted"}
