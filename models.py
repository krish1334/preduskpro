from sqlalchemy import Column, Integer, String
from database import Base

class Profile(Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    education = Column(String)
    skills = Column(String)  # comma-separated

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    skills = Column(String)
    link = Column(String)
