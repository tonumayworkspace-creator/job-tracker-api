from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.models import User, Job
from app.schemas.schemas import UserCreate, UserResponse, JobCreate, JobResponse
from app.utils.utils import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user
)

router = APIRouter()


# =========================
# AUTH APIs
# =========================

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    hashed_pwd = hash_password(user.password)

    new_user = User(
        email=user.email,
        password=hashed_pwd
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": db_user.email})

    return {"access_token": token, "token_type": "bearer"}


# =========================
# USER APIs
# =========================

@router.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


# =========================
# JOB APIs (SECURED)
# =========================

# CREATE JOB (ONLY LOGGED-IN USER)
@router.post("/jobs", response_model=JobResponse)
def create_job(
    job: JobCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    new_job = Job(
        company=job.company,
        role=job.role,
        status=job.status,
        owner_id=current_user.id
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job


# GET USER'S JOBS ONLY
@router.get("/jobs", response_model=list[JobResponse])
def get_jobs(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(Job).filter(Job.owner_id == current_user.id).all()


# FILTER USER'S JOBS
@router.get("/jobs/filter", response_model=list[JobResponse])
def filter_jobs(
    status: str = Query(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(Job).filter(
        Job.status == status,
        Job.owner_id == current_user.id
    ).all()


# UPDATE JOB (ONLY OWNER)
@router.put("/jobs/{job_id}", response_model=JobResponse)
def update_job(
    job_id: int,
    updated_job: JobCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    job = db.query(Job).filter(
        Job.id == job_id,
        Job.owner_id == current_user.id
    ).first()

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    job.company = updated_job.company
    job.role = updated_job.role
    job.status = updated_job.status

    db.commit()
    db.refresh(job)

    return job


# DELETE JOB (ONLY OWNER)
@router.delete("/jobs/{job_id}")
def delete_job(
    job_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    job = db.query(Job).filter(
        Job.id == job_id,
        Job.owner_id == current_user.id
    ).first()

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    db.delete(job)
    db.commit()

    return {"message": "Job deleted successfully"}