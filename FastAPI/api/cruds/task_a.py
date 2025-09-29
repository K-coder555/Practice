from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
import api.models.task_a as task_model
import api.schemas.task_a as task_schema
async def create_task(db: AsyncSession, task_create: task_schema.TaskCreate) -> task_schema.TaskCreateResponse:
    task = task_model.Task(**task_create.model_dump())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    # 새로 만든 task는 당연히 done이 False
    return task_schema.TaskCreateResponse(id=task.id, title=task.title, done=False)
async def get_tasks_with_done(db: AsyncSession) -> list[task_schema.Task]:
    result = await db.execute(
        select(
            task_model.Task.id,
            task_model.Task.title,
            (task_model.Done.id.isnot(None)).label("done")
        ).outerjoin(task_model.Done, task_model.Task.id == task_model.Done.id)
    )
    tasks = result.all()
    return [task_schema.Task(id=id_, title=title, done=done) for id_, title, done in tasks]
async def get_task(db: AsyncSession, task_id: int) -> task_model.Task | None:
    result = await db.execute(
        select(task_model.Task).where(task_model.Task.id == task_id)
    )
    return result.scalars().first()
async def update_task(db: AsyncSession, task_create: task_schema.TaskCreate, original: task_model.Task) -> task_schema.TaskCreateResponse:
    original.title = task_create.title
    db.add(original)
    await db.commit()
    await db.refresh(original)
    # done 여부는 외부에서 조회
    result = await db.execute(
        select(task_model.Done.id).where(task_model.Done.id == original.id)
    )
    done_exists = result.scalar() is not None
    return task_schema.TaskCreateResponse(id=original.id, title=original.title, done=done_exists)
async def delete_task(db: AsyncSession, original: task_model.Task) -> None:
    await db.delete(original)
    await db.commit()