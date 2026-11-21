from src.task.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.task.models import TaskModel
from fastapi import HTTPException
from src.user.models import UserModel

def create_task(body:TaskSchema,db:Session,user:UserModel):
    data = body.model_dump()
    new_task = TaskModel(title=data['title'],description=data['description'],is_completed=data['is_completed'],user_id=user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_all_tasks(db:Session,user:UserModel):
    tasks = db.query(TaskModel).filter(TaskModel.user_id == user.id).all()
    return tasks

def get_one_task(task_id:int,db:Session,user:UserModel):
    one_task = db.query(TaskModel).filter(TaskModel.id == task_id, TaskModel.user_id == user.id).first()
    if not one_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return one_task

def update_task(body:TaskSchema,task_id:int,db:Session,user:UserModel):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(status_code=404, detail="Task not found")
    if one_task.user_id != user.id:
        raise HTTPException(status_code=403, detail="You are not authorized to update this task")
    # one_task.title = body.title
    # one_task.description = body.description
    # one_task.is_completed = body.is_completed
    body = body.model_dump()
    for field, value in body.items():
        setattr(one_task, field, value)
    db.add(one_task)
    db.commit()
    db.refresh(one_task)
    return one_task

def delete_task(task_id:int, db:Session, user:UserModel):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail="Task Id is Incorrect")
    if one_task.user_id != user.id:
            raise HTTPException(status_code=403, detail="You are not authorized to delete this task")
    db.delete(one_task)
    db.commit()

    return None