from fastapi import APIRouter, Depends
from src.task import controller
from src.task.dtos import TaskSchema
from src.utils.db import get_db

task_router = APIRouter(prefix="/tasks") #"https://127.0.0.1:8000/tasks"

@task_router.post("/create")
def create_task(body:TaskSchema,db = Depends(get_db)):
    return controller.create_task(body,db)

@task_router.get("/all_tasks")
def get_all_tasks(db = Depends(get_db)):
    return controller.get_all_tasks(db)