from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from database import Base
import datetime

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    appointment_time = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String(50), default="pending")  # pending, confirmed, cancelled

    patient = relationship("Patient")
    doctor = relationship("Doctor")
