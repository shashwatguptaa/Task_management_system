from fastapi import APIRouter, Depends,status
from src.task import controller
from src.task.dtos import TaskSchema, TaskResponseSchema
from src.utils.db import get_db
from sqlalchemy.orm import Session
from typing import List

task_router = APIRouter(prefix="/tasks") #"https://127.0.0.1:8000/tasks"

@task_router.post("/create",response_model = TaskResponseSchema,status_code = status.HTTP_201_CREATED)
def create_task(body:TaskSchema,db:Session = Depends(get_db)):
    return controller.create_task(body,db)

@task_router.get("/all_tasks",response_model = List[TaskResponseSchema],status_code = status.HTTP_200_OK)
def get_all_tasks(db:Session = Depends(get_db)):
    return controller.get_all_tasks(db)

@task_router.get("/get_task/{task_id}",response_model = TaskResponseSchema,status_code = status.HTTP_200_OK)
def get_one_task(task_id:int,db:Session = Depends(get_db)):
    return controller.get_one_task(task_id,db)


@task_router.put("/update_task/{task_id}",response_model = TaskResponseSchema,status_code = status.HTTP_201_CREATED)
def update_task(body:TaskSchema,task_id:int,db:Session = Depends(get_db)):
    return controller.update_task(body,task_id,db)


@task_router.delete("/delete_task/{task_id}",response_model = None,status_code = status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int,db:Session = Depends(get_db)):
    return controller.delete_task(task_id,db)