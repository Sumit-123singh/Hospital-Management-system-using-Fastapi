# Hospital-Management-system-using-Fastapi
This is a full-featured Hospital Management System built using FastAPI, designed to streamline and manage the day-to-day operations of a hospital or clinic. It provides secure APIs for handling doctors, patients, appointments, medical records, and users with role-based access (admin, staff, doctor, etc.).




# 🏥 Hospital Management System API (FastAPI + SQLAlchemy + MySQL)

A modern **Hospital Management System (HMS)** backend built using **FastAPI**, **Pydantic**, and **SQLAlchemy**, designed to manage doctors, patients, appointments, users (staff/admin), and medical records efficiently.

---

## 🚀 Features

- ✅ Add, update, and retrieve **patient** data  
- ✅ Manage **doctors** and their specialization  
- ✅ Book and track **appointments**  
- ✅ Maintain **medical records** for each patient  
- ✅ Register **users** (e.g., admin/staff) for controlled access *(no authentication system yet)*  
- ✅ Built with **FastAPI** for speed and simplicity  
- ✅ Follows **clean architecture** with `models`, `schemas`, `routes`






## 🧪 Use Cases

| Module           | Functionality                                                                 |
|------------------|------------------------------------------------------------------------------|
| 👨‍⚕️ Doctor        | Add/update doctor profiles, view all/specialization-based doctors           |
| 🧑 Patient         | Register patients, update records, fetch patient list/details               |
| 📅 Appointment     | Book appointments by doctor & patient IDs, track appointments              |
| 📋 Medical Record  | Add/fetch patient medical history (e.g., diagnoses, prescriptions)         |
| 🔐 User            | Register backend users (admin/staff)                                        |

---

📁 Project Structure
hospital_management/
├── __pycache__/                    # Auto-generated Python cache files

├── models/                         # SQLAlchemy ORM models (database tables)
│   ├── patient.py                  # Patient model (name, age, etc.)
│   ├── doctor.py                   # Doctor model (specialization, etc.)
│   ├── appointment.py              # Appointment model (patient-doctor bookings)
│   ├── user.py                     # User model for admin/staff authentication
│   ├── medical_record.py           # Medical history model for patients
│   └── __init__.py                 # Makes models a Python package

├── routes/                         # FastAPI route handlers (API endpoints)
│   ├── patient.py                  # CRUD endpoints for patient
│   ├── doctor.py                   # CRUD endpoints for doctor
│   ├── appointment.py              # Endpoints to book/view appointments
│   ├── user.py                     # Auth routes for admin/staff
│   ├── medical_record.py           # Endpoints to manage patient records
│   └── __init__.py                 # Makes routes a Python package

├── schemas/                        # Pydantic models for validation/serialization
│   ├── patient.py                  # Patient request/response schema
│   ├── doctor.py                   # Doctor request/response schema
│   ├── appointment.py              # Appointment schema
│   ├── user.py                     # User schema (e.g., login data)
│   ├── medical_record.py           # Schema for medical history
│   └── __init__.py                 # Makes schemas a Python package

├── database.py                     # SQLAlchemy DB setup using MySQL engine

├── main.py                         # FastAPI application entry point

├── requirements.txt                # All required Python packages

└── README.md                       # Project documentation



## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Sumit-123singh/Hospital-Management-system-using-Fastapi
cd hospital_management

2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies
pip install -r requirements.txt

4. Set up your database
Make sure MySQL is running
Create a database named hospital_db or your preferred name
Update the DB connection URL in database.py:
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://username:password@localhost/hospital_db"

5. Run the FastAPI server
uvicorn main:app --reload
Visit the docs at 👉 http://localhost:8000/docs





hospital_management/
├── __pycache__/                    # Python bytecode cache (auto-generated)

├── models/                         # SQLAlchemy ORM models
│   ├── patient.py
│   ├── doctor.py
│   ├── appointment.py
│   ├── user.py
│   ├── medical_record.py
│   └── __init__.py

├── routes/                         # API route handlers
│   ├── patient.py
│   ├── doctor.py
│   ├── appointment.py
│   ├── user.py
│   ├── medical_record.py
│   └── __init__.py

├── schemas/                        # Pydantic request/response models
│   ├── patient.py
│   ├── doctor.py
│   ├── appointment.py
│   ├── user.py
│   ├── medical_record.py
│   └── __init__.py

├── database.py                     # SQLAlchemy DB setup (MySQL engine)
├── main.py                         # FastAPI app entry point
├── requirements.txt                # All Python dependencies
└── README.md                       # Project documentation


🧑‍💻 Author
Sumit Singh
ML Enthusiast | Backend Developer



