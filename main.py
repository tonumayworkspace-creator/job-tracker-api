from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import engine, Base
from app.models import models
from app.api.routes import router

app = FastAPI()

# ✅ CORS CONFIG (IMPORTANT)
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

# Routes
app.include_router(router)


@app.get("/")
def root():
    return {"message": "Job Tracker API is running 🚀"}