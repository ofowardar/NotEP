from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app import models
from app.routers import notes, auth
from app.logging_config import logger

logger.info("Application Starting...")

# Tabloları oluştur
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Notes API", version="1.0")

# CORS setup - en başta!
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000", 
        "http://localhost:5173",
        "https://notep-frontend-iy2pgoumt-ofo1.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router'ları kayıt et
app.include_router(auth.router)
app.include_router(notes.router)

logger.info("Application started successfully")

@app.get("/")
def root_check():
    return {"message": "Root Check Worked!"}