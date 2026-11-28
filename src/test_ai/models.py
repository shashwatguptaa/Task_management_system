from src.utils.db import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey

class TaskModel(Base):
    __tablename__ = "user_tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255),nullable=False)
    description = Column(String(500),default="")
    status = Column(String(50),default="pending") ##pending|in_progress|completed
    priority = Column(String(50),default="medium") ##low|medium|high
    due_date = Column(DateTime,nullable=True)
    created_at = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("user_table.id",ondelete="CASCADE"),nullable=False,index=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "created_at": self.created_at.isoformat(),
            "user_id": self.user_id
        }