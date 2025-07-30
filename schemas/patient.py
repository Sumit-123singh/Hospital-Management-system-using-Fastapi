from pydantic import BaseModel
from typing import Optional

class PatientBase(BaseModel):
    full_name: str
    age: int
    gender: str
    address: Optional[str] = None

class PatientCreate(PatientBase):
    user_id: int

class PatientResponse(PatientBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
