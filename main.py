from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/form_data/saveKpaData", response_model=schemas.KpaDataOut)
def save_kpa(data: schemas.KpaDataCreate, db: Session = Depends(get_db)):
    return crud.create_kpa_data(db, data)

@app.get("/form_data/getAllKpaData", response_model=list[schemas.KpaDataOut])
def get_all_kpa(db: Session = Depends(get_db)):
    return crud.get_all_kpa_data(db)
