from fastapi import APIRouter
from src.routes.students import router as student_router

router = APIRouter()

router.include_router(student_router)
