from src.utils.db import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime

class TaskModel(Base):
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    hash_password = Column(String, nullable=False)
    email = Column(String)