from pydantic import BaseModel, Field

class NoteCreate(BaseModel):
    title:str = Field(min_length=1,max_length=100)
    content:str = Field(min_length=1,max_length=500)

class NoteResponse(NoteCreate):
    id:int

    