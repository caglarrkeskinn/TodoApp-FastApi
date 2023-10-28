from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"  # You can adjust this URL for other databases

Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=True)  # `echo=True` for logging SQL statements, can be turned off in production
SessionLocal = sessionmaker(bind=engine)

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, index=True)
    completed = Column(Boolean, default=False)