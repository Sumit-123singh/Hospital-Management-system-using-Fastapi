from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.patient import PatientCreate, PatientResponse
from models.patient import Patient
from database import get_db

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.post("/", response_model=PatientResponse)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    db_patient = Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

@router.get("/", response_model=list[PatientResponse])
def get_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all()
