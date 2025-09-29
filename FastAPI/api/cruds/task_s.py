from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.task_a as task_model
import api.schemas.task_a as task_schema

def create_task(db: Session, task_create: task_schema.TaskCreate) -> task_model.Task:
    task = task_model.Task(**task_create.model_dump())  # Pydantic v2
    db.add(task)
    db.commit()
    db.refresh(task)  # 줄바꿈 및 refresh 호출 수정
    return task

def get_tasks_with_done(db: Session) -> list[task_schema.Task]:
    result: Result = db.execute(
        select(
            task_model.Task.id,
            task_model.Task.title,
            (task_model.Done.id.isnot(None)).label("done")  # Done 테이블이 존재할 경우
        ).outerjoin(task_model.Done)
    )
    
    tasks = result.all()
    
    # SQLAlchemy의 raw tuple을 Pydantic 모델로 변환
    return [task_schema.Task(id=t[0], title=t[1], done=t[2]) for t in tasks]

def get_task(db: Session, task_id: int) -> task_model.Task | None:
    result: Result = db.execute( select(task_model.Task).where(task_model.Task.id == task_id)
    )
    return result.scalars().first()

def update_task(
        db: Session, task_create: task_schema.TaskCreate, original:task_model.Task) -> task_model.Task:
        original.title = task_create.title
        db.add(original)
        db.commit()
        db.refresh(original)
        return original

def delete_task(db: Session, original: task_model.Task) -> None:
    db.delete(original)
    db.commit()

