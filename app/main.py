from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.dosen import main as dosen_main
from app.histori_jadwal  import main as jadwal_history_main
from app.integrasi_kalender import  main as kalender_integrasi_main
from app.kelas import main as kelas_main
from app.ketersediaan_dosen import main as ketersediaan_dosen_main
from app.mata_kuliah import main as mata_kuliah_main
from app.ruangan import main as ruangan_main

from .database import engine, SessionLocal

app = FastAPI()

app.include_router(dosen_main.router, prefix="/dosen")
app.include_router(jadwal_history_main.router, prefix="/histori_jadwal")
app.include_router(kalender_integrasi_main.router, prefix="/integrasi_kalender")
app.include_router(kelas_main.router, prefix="/kelas")
app.include_router(ketersediaan_dosen.router, prefix="/ketersediaan_dosen")
app.include_router(mata_kuliah_main.router, prefix="/mata_kuliah")
app.include_router(ruangan_main.router, prefix="/ruangan")

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
