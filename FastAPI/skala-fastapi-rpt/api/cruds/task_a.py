from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.task_a as task_model
import api.schemas.task_a as task_schema

async def create_task(db: AsyncSession, task_create: task_schema.TaskCreate) -> task_model.Task:
    task = task_model.Task(**task_create.model_dump())  
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

async def get_tasks_with_done(db: AsyncSession) -> list[task_schema.Task]:
    result = await db.execute(  # ✅ `await` 추가
        select(
            task_model.Task.id,
            task_model.Task.title,
            (task_model.Done.id.isnot(None)).label("done")
        ).outerjoin(task_model.Done)
    )
    tasks = result.all()  # ✅ `await` 필요 없음 (execute는 `await` 처리됨)
    return [task_schema.Task(id=t[0], title=t[1], done=t[2]) for t in tasks]

async def get_task(db: AsyncSession, task_id: int) -> task_model.Task | None:
    result = await db.execute(  # ✅ `await` 추가
        select(task_model.Task).where(task_model.Task.id == task_id)
    )
    return result.scalars().first()

async def update_task(db: AsyncSession, task_create: task_schema.TaskCreate, original: task_model.Task) -> task_model.Task:
    original.title = task_create.title
    db.add(original)
    await db.commit()  # ✅ `await` 추가
    await db.refresh(original)  # ✅ `await` 추가
    return original

async def delete_task(db: AsyncSession, original: task_model.Task) -> None:
    await db.delete(original)  # ✅ `await` 추가
    await db.commit()  # ✅ `await` 추가
