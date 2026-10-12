from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Note, User
from app.schemas import NoteCreate, NoteResponse, PaginatedNotes
from app.security import get_current_user

router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
def create_note(note: NoteCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    # Note'u oluştur ve user_id'yi set et
    db_note = Note(title=note.title, content=note.content, user_id=current_user["user_id"])
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


@router.get("", response_model=PaginatedNotes)
def list_notes(skip: int = 0, limit: int = 10, search: str = None, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    # Sadece kendi notlarını getir
    query = db.query(Note).filter(Note.user_id == current_user["user_id"])
    
    if search:
        query = query.filter(Note.title.ilike(f"%{search}%"))
    
    total = query.count()
    notes = query.offset(skip).limit(limit).all()
    
    return {"total": total, "skip": skip, "limit": limit, "items": notes}


@router.get("/{note_id}", response_model=NoteResponse)
def get_note(note_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    note = db.query(Note).filter(Note.id == note_id, Note.user_id == current_user["user_id"]).first()
    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not bulunamadı"
        )
    return note


@router.put("/{note_id}", response_model=NoteResponse)
def update_note(note_id: int, note: NoteCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_note = db.query(Note).filter(Note.id == note_id, Note.user_id == current_user["user_id"]).first()
    if db_note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not bulunamadı"
        )
    db_note.title = note.title
    db_note.content = note.content
    db.commit()
    db.refresh(db_note)
    return db_note


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_note = db.query(Note).filter(Note.id == note_id, Note.user_id == current_user["user_id"]).first()
    if db_note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not bulunamadı"
        )
    db.delete(db_note)
    db.commit()