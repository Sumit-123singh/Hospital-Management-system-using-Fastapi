from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_time: Optional[datetime] = None
    status: Optional[str] = "pending"

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentResponse(AppointmentBase):
    id: int

    class Config:
        orm_mode = True
