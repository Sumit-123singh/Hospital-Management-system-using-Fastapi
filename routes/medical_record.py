from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.medical_record import MedicalRecordCreate, MedicalRecordResponse
from models.medical_record import MedicalRecord
from database import get_db
from datetime import datetime

router = APIRouter(prefix="/records", tags=["Medical Records"])

@router.post("/", response_model=MedicalRecordResponse)
def create_record(record: MedicalRecordCreate, db: Session = Depends(get_db)):
    db_record = MedicalRecord(**record.model_dump(), created_at=datetime.utcnow())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

@router.get("/", response_model=list[MedicalRecordResponse])
def get_records(db: Session = Depends(get_db)):
    return db.query(MedicalRecord).all()
