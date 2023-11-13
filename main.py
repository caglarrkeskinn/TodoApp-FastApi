from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
from schemas import Todo, TodoCreate
from typing import List

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Initialize the database
models.Base.metadata.create_all(bind=models.engine)

# Dependency to get the database session
def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/todos/", response_model=Todo)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = models.Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.get("/todos/", response_model=List[Todo])
def list_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Todo).offset(skip).limit(limit).all()

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return todo

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    for key, value in todo.dict().items():
        setattr(db_todo, key, value)
    
    db.commit()
    db.refresh(db_todo)
    return db_todo
