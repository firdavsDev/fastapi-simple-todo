from fastapi import APIRouter

from app.api.v1.endpoints import todo

router = APIRouter()

# Barcha marshrutlarni qo'shamiz
router.include_router(todo.router, prefix="/todos", tags=["Todos"])
