from pydantic import BaseModel
from typing import Optional

class DoctorBase(BaseModel):
    full_name: str
    specialty: str
    experience_years: int

class DoctorCreate(DoctorBase):
    user_id: int

class DoctorResponse(DoctorBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
