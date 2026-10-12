from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from app.database import get_db
from app.models import Note, User
from app.schemas import NoteCreate, NoteResponse, PaginatedNotes
from app.security import get_current_user
from app.logging_config import logger

router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
def create_note(note: NoteCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    logger.info(f"User {current_user['user_id']} creating note: {note.title}")
    now = datetime.now(timezone.utc)
    db_note = Note(title=note.title, content=note.content, user_id=current_user["user_id"], updated_at=now)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    logger.info(f"Note created successfully: ID {db_note.id} for user {current_user['user_id']}")
    return db_note


@router.get("", response_model=PaginatedNotes)
def list_notes(skip: int = 0, limit: int = 10, search: str = None, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    logger.info(f"User {current_user['user_id']} listing notes: skip={skip}, limit={limit}, search={search}")
    query = db.query(Note).filter(Note.user_id == current_user["user_id"])
    
    if search:
        query = query.filter(Note.title.ilike(f"%{search}%"))
    
    total = query.count()
    notes = query.offset(skip).limit(limit).all()
    logger.info(f"Retrieved {len(notes)} notes for user {current_user['user_id']}")
    
    return {"total": total, "skip": skip, "limit": limit, "items": notes}


@router.get("/{note_id}", response_model=NoteResponse)
def get_note(note_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    logger.info(f"User {current_user['user_id']} fetching note: {note_id}")
    note = db.query(Note).filter(Note.id == note_id, Note.user_id == current_user["user_id"]).first()
    if note is None:
        logger.warning(f"Note {note_id} not found or unauthorized for user {current_user['user_id']}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not bulunamadı"
        )
    logger.info(f"Note {note_id} fetched successfully for user {current_user['user_id']}")
    return note


@router.put("/{note_id}", response_model=NoteResponse)
def update_note(note_id: int, note: NoteCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    logger.info(f"User {current_user['user_id']} updating note: {note_id}")
    db_note = db.query(Note).filter(Note.id == note_id, Note.user_id == current_user["user_id"]).first()
    if db_note is None:
        logger.warning(f"Update failed: Note {note_id} not found or unauthorized for user {current_user['user_id']}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not bulunamadı"
        )
    db_note.title = note.title
    db_note.content = note.content
    db.commit()
    db.refresh(db_note)
    logger.info(f"Note {note_id} updated successfully for user {current_user['user_id']}")
    return db_note


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    logger.info(f"User {current_user['user_id']} deleting note: {note_id}")
    db_note = db.query(Note).filter(Note.id == note_id, Note.user_id == current_user["user_id"]).first()
    if db_note is None:
        logger.warning(f"Delete failed: Note {note_id} not found or unauthorized for user {current_user['user_id']}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not bulunamadı"
        )
    db.delete(db_note)
    db.commit()
    logger.info(f"Note {note_id} deleted successfully for user {current_user['user_id']}")