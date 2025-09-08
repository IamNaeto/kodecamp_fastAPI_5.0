from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from pathlib import Path
import json

from .. import models, schemas, auth
from ..database import get_session

router = APIRouter(prefix="/contacts", tags=["contacts"])
BACKUP_FILE = Path(__file__).resolve().parent.parent / "backups" / "contacts.json"
BACKUP_FILE.parent.mkdir(parents=True, exist_ok=True)
if not BACKUP_FILE.exists():
    BACKUP_FILE.write_text("[]")


def save_backup(contacts: List[models.Contact]):
    # convert created_at to iso strings
    data = []
    for c in contacts:
        d = c.dict()
        d["created_at"] = d["created_at"].isoformat()
        data.append(d)
    BACKUP_FILE.write_text(json.dumps(data, indent=2))


@router.post("/", response_model=schemas.ContactRead)
def create_contact(contact_in: schemas.ContactCreate, session: Session = Depends(get_session), current_user: models.User = Depends(auth.get_current_user)):
    contact = models.Contact(**contact_in.dict(), user_id=current_user.id)
    session.add(contact)
    session.commit()
    session.refresh(contact)

    all_contacts = session.exec(select(models.Contact).where(models.Contact.user_id == current_user.id)).all()
    save_backup(all_contacts)
    return contact


@router.get("/", response_model=List[schemas.ContactRead])
def list_contacts(session: Session = Depends(get_session), current_user: models.User = Depends(auth.get_current_user)):
    contacts = session.exec(select(models.Contact).where(models.Contact.user_id == current_user.id)).all()
    return contacts


@router.put("/{contact_id}", response_model=schemas.ContactRead)
def update_contact(contact_id: int, contact_update: schemas.ContactUpdate, session: Session = Depends(get_session), current_user: models.User = Depends(auth.get_current_user)):
    contact = session.get(models.Contact, contact_id)
    if not contact or contact.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Contact not found")
    contact_data = contact_update.dict(exclude_unset=True)
    for k, v in contact_data.items():
        setattr(contact, k, v)
    session.add(contact)
    session.commit()
    session.refresh(contact)

    all_contacts = session.exec(select(models.Contact).where(models.Contact.user_id == current_user.id)).all()
    save_backup(all_contacts)
    return contact


@router.delete("/{contact_id}", status_code=204)
def delete_contact(contact_id: int, session: Session = Depends(get_session), current_user: models.User = Depends(auth.get_current_user)):
    contact = session.get(models.Contact, contact_id)
    if not contact or contact.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Contact not found")
    session.delete(contact)
    session.commit()

    all_contacts = session.exec(select(models.Contact).where(models.Contact.user_id == current_user.id)).all()
    save_backup(all_contacts)
    return None
