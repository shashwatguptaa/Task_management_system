from src.utils.db import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime

class TaskModel(Base):
    __tablename__ = "user_tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(String(255))
    is_completed = Column(Boolean, default=False)