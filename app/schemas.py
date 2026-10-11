from pydantic import BaseModel, Field
from datetime import datetime

class NoteCreate(BaseModel):
    title:str = Field(min_length=1,max_length=100)
    content:str = Field(min_length=1,max_length=500)

class NoteResponse(NoteCreate):
    id:int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

    