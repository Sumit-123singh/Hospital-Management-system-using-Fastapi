from fastapi import FastAPI
from database import Base, engine
from routes import user, patient, doctor, appointment, medical_record

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(patient.router)
app.include_router(doctor.router)
app.include_router(appointment.router)
app.include_router(medical_record.router)

@app.get("/")
def read_root():
    return {"message": "Hospital Management System API Running"}
