from fastapi import FastAPI
from src.utils.db import get_db,Base,engine
from src.task.router import task_router

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Task Management API")
app.include_router(task_router)