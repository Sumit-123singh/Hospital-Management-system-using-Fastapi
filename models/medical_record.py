from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import datetime

class MedicalRecord(Base):
    __tablename__ = "medical_records"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    diagnosis = Column(String(255))
    treatment = Column(String(255))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    patient = relationship("Patient")
    doctor = relationship("Doctor")
