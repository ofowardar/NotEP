from pydantic import BaseModel, Field
from datetime import datetime


class NoteCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str


class NoteResponse(NoteCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class PaginatedNotes(BaseModel):
    total: int
    skip: int
    limit: int
    items: list[NoteResponse]


class UserCreate(BaseModel):
    email:str
    password:str

class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token:str
    token_type:str

