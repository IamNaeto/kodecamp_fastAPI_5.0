from __future__ import annotations
from sqlmodel import SQLModel, create_engine, Session
import os

DB_URL = os.getenv("DATABASE_URL", "sqlite:///./student.db")
connect_args = {"check_same_thread": False} if DB_URL.startswith("sqlite") else {}
engine = create_engine(DB_URL, echo=False, connect_args=connect_args)


def init_db() -> None:
    """Create DB tables."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    with Session(engine) as session:
        yield session
