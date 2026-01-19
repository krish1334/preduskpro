from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Profile, Project, Base
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Me-API Playground")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/profile")
def get_profile(db: Session = Depends(get_db)):
    return db.query(Profile).first()

@app.put("/profile")
def update_profile(data: dict, db: Session = Depends(get_db)):
    profile = db.query(Profile).first()
    for k, v in data.items():
        setattr(profile, k, v)
    db.commit()
    return profile

@app.get("/projects")
def get_projects(skill: str | None = None, db: Session = Depends(get_db)):
    q = db.query(Project)
    if skill:
        q = q.filter(Project.skills.like(f"%{skill}%"))
    return q.all()

@app.get("/skills/top")
def top_skills(db: Session = Depends(get_db)):
    profile = db.query(Profile).first()
    return profile.skills.split(",")

@app.get("/search")
def search(q: str, db: Session = Depends(get_db)):
    return db.query(Project).filter(
        Project.title.like(f"%{q}%") |
        Project.description.like(f"%{q}%")
    ).all()
