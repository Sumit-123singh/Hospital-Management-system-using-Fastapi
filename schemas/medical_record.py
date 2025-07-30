from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MedicalRecordBase(BaseModel):
    patient_id: int
    doctor_id: int
    diagnosis: str
    treatment: str

class MedicalRecordCreate(MedicalRecordBase):
    pass

class MedicalRecordResponse(MedicalRecordBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
