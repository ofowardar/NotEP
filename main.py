from fastapi import FastAPI,status,HTTPException
from schemas import NoteCreate,NoteResponse

app = FastAPI()


notes_db:dict[int,dict] = {}

next_id = 1

@app.get("/")
def root_check():
    return {"message":"Root Check Worked!"}

@app.post("/notes",response_model=NoteResponse,status_code=status.HTTP_201_CREATED)
def create_note(note:NoteCreate):
    global next_id
    new_note = {"id":next_id, **note.model_dump()}
    notes_db[next_id] = new_note
    next_id+=1
    return new_note

@app.get("/notes",response_model=list[NoteResponse])
def list_notes():
    return list(notes_db.values())

@app.get("/notes/{note_id}", response_model=NoteResponse)
def get_note(note_id:int):
    note = notes_db.get(note_id)
    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = f"{note_id} . note is not found!!"
        )
    return note

@app.delete("/notes/{note_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id:int):
    note = notes_db.get(note_id)
    if note is None:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )
    notes_db.pop(note_id)

@app.put("/notes/{note_id}", response_model=NoteResponse)
def update_note(note_id:int,note:NoteCreate):
    current_note = notes_db.get(note_id)
    if current_note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note {note_id} is not found.!"
        )
    updated_note = {"id":note_id,**note.model_dump()}
    notes_db[note_id] = updated_note
    return updated_note