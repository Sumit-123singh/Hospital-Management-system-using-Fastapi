from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.doctor import DoctorCreate, DoctorResponse
from models.doctor import Doctor
from database import get_db

router = APIRouter(prefix="/doctors", tags=["Doctors"])

@router.post("/", response_model=DoctorResponse)
def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    db_doctor = Doctor(**doctor.dict())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

@router.get("/", response_model=list[DoctorResponse])
def get_doctors(db: Session = Depends(get_db)):
    return db.query(Doctor).all()
