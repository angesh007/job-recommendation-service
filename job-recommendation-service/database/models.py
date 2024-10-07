from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class UserProfile(Base):
    __tablename__ = 'user_profiles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    skills = Column(Text, nullable=False)  # Comma-separated string of skills
    experience_level = Column(String(20), nullable=False)
    preferences = Column(Text, nullable=False)  # JSON string for preferences

    def __repr__(self):
        return f"<UserProfile(name='{self.name}', experience_level='{self.experience_level}')>"


class JobPosting(Base):
    __tablename__ = 'job_postings'

    job_id = Column(Integer, primary_key=True, autoincrement=True)
    job_title = Column(String(100), nullable=False)
    company = Column(String(100), nullable=False)
    required_skills = Column(Text, nullable=False)  # Comma-separated string of required skills
    location = Column(String(100), nullable=False)
    job_type = Column(String(50), nullable=False)
    experience_level = Column(String(20), nullable=False)

    def __repr__(self):
        return f"<JobPosting(job_title='{self.job_title}', company='{self.company}')>"

# Creating the engine for the SQLite database
def get_engine(db_name='jobs.db'):
    return create_engine(f'sqlite:///{db_name}')

# Creating the tables
def create_tables():
    engine = get_engine()
    Base.metadata.create_all(engine)

