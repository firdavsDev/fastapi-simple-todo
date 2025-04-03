from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.todo import TodoCreate, TodoResponse
from app.services.todo_service import create_todo, get_todo, get_todos

router = APIRouter()


@router.post("/", response_model=TodoResponse)
def create_todo_api(todo: TodoCreate, db: Session = Depends(get_db)):
    return create_todo(db, todo)


@router.get("/", response_model=list[TodoResponse])
def get_all_todos_api(db: Session = Depends(get_db)):
    return get_todos(db)


# @router.get("/", response_model=PaginatedResponse[TodoResponse])
# def get_all_todos_api(
#     request: Request,
#     db: Session = Depends(get_db),
#     limit: int = Query(10, alias="limit"),
#     offset: int = Query(0, alias="offset"),
# ):
#     total = db.query(Todo).count()
#     todos = db.query(Todo).offset(offset).limit(limit).all()

#     return PaginatedResponse.create(todos, total, limit, offset, request)


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo_api(todo_id: int, db: Session = Depends(get_db)):
    todo = get_todo(db, todo_id)
    if todo:
        return todo
    raise HTTPException(status_code=404, detail="Todo not found")
