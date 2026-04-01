from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# =========================
# USER SCHEMAS
# =========================

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True


# =========================
# JOB SCHEMAS
# =========================

class JobCreate(BaseModel):
    company: str
    role: str
    status: Optional[str] = "Applied"


class JobResponse(BaseModel):
    id: int
    company: str
    role: str
    status: str
    created_at: datetime
    owner_id: int

    class Config:
        from_attributes = True