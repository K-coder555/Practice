from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
# from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import declarative_base

# Base = declarative_base(cls=AsyncAttrs)
from api.db_a import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(1024))

    done = relationship(
        "Done",
        back_populates="task",
        cascade="all, delete-orphan",
        lazy="selectin"  # ✅ 비동기 처리를 위해 lazy="selectin" 사용
    )

class Done(Base):
    __tablename__ = "dones"

    id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)

    task = relationship(
        "Task",
        back_populates="done",
        lazy="selectin"  # ✅ 비동기 처리를 위해 lazy="selectin" 사용
    )
