from fastapi import FastAPI
from app.database import engine, Base
from app import models  # ← BU SATIRI EKLE
from app.routers import notes, auth
from fastapi.middleware.cors import CORSMiddleware
# Tabloları oluştur
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Notes API", version="1.0")


#CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Router'ları kayıt et
app.include_router(auth.router)
app.include_router(notes.router)


@app.get("/")
def root_check():
    return {"message": "Root Check Worked!"}