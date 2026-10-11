from sqlalchemy import Column,Integer,String,Text,DateTime
from sqlalchemy.sql import func
from app.database import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(100),nullable=False)
    content = Column(Text)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

