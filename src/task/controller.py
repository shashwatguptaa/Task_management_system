from src.task.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.task.models import TaskModel

def create_task(body:TaskSchema,db:Session):
    data = body.model_dump()
    new_task = TaskModel(title=data['title'],description=data['description'],is_completed=data['is_completed'])
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"status":"success","message":"Task created successfully","data":new_task}

def get_all_tasks(db:Session):
    tasks = db.query(TaskModel).all()
    return {"status":"success","message":"Tasks fetched successfully","data":tasks}