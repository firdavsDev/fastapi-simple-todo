from sqlalchemy.orm import Session

from app.db.models import Todo
from app.schemas.todo import TodoCreate


def create_todo(db: Session, todo: TodoCreate):
    db_todo = Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


# def get_todos(db: Session, skip: int, limit: int):
#     return db.query(Todo).offset(skip).limit(limit).all()


def get_todos(db: Session):
    return db.query(Todo).all()


def get_todo(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()
