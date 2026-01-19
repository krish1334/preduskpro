from database import engine, SessionLocal
from models import Base, Profile, Project

Base.metadata.create_all(bind=engine)
db = SessionLocal()

db.query(Profile).delete()
db.query(Project).delete()

profile = Profile(
    name="Krishna Sunil",
    email="krishnasunilo51@gmail.com",
    education="NIT Delhi/M.Tech",
    skills="python,fastapi,sql,backend"
)

projects = [
    Project(
        title="Me API Playground",
        description="Backend API with FastAPI and SQLite",
        skills="python,fastapi,backend",
        link="https://github.com/yourname/me-api"
    )
]

db.add(profile)
for p in projects:
    db.add(p)

db.commit()
db.close()
print("Seeded successfully")
