from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List, Optional
import json
from pathlib import Path

from ..database import get_session
from ..models import JobApplication
from ..auth import get_current_user, User

router = APIRouter(prefix="/applications", tags=["applications"])

BACKUP_FILE = Path(__file__).resolve().parent.parent / "backups" / "applications.json"

# 🔄 Save applications to JSON backup
def save_backup(applications: list[JobApplication]):
    data = [app.dict() for app in applications]
    BACKUP_FILE.write_text(json.dumps(data, indent=4))

# ✅ Create a new job application
@router.post("/", response_model=JobApplication)
def create_application(
    application: JobApplication,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    application.user_id = current_user.id
    session.add(application)
    session.commit()
    session.refresh(application)

    apps = session.exec(select(JobApplication).where(JobApplication.user_id == current_user.id)).all()
    save_backup(apps)

    return application

# ✅ List all applications
@router.get("/", response_model=List[JobApplication])
def list_applications(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    apps = session.exec(select(JobApplication).where(JobApplication.user_id == current_user.id)).all()
    if not apps:
        raise HTTPException(status_code=404, detail="No applications found")
    return apps

# ✅ Search applications
@router.get("/search", response_model=List[JobApplication])
def search_applications(
    status: Optional[str] = None,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    query = select(JobApplication).where(JobApplication.user_id == current_user.id)

    if status:
        query = query.where(JobApplication.status == status)

    results = session.exec(query).all()
    if not results:
        raise HTTPException(status_code=404, detail="No applications found")

    return results
