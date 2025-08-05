from sqlalchemy.orm import Session
import models, schemas

def create_kpa_data(db: Session, data: schemas.KpaDataCreate):
    db_data = models.KpaData(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def get_all_kpa_data(db: Session):
    return db.query(models.KpaData).all()
