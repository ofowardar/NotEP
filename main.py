from fastapi import FastAPI
from app.database import engine, Base
from app import models  # ← BU SATIRI EKLE
from app.routers import notes, auth

# Tabloları oluştur
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Notes API", version="1.0")

# Router'ları kayıt et
app.include_router(auth.router)
app.include_router(notes.router)


@app.get("/")
def root_check():
    return {"message": "Root Check Worked!"}