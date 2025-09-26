from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
import api.models.task_a as task_model

async def get_done(db: AsyncSession, task_id: int) -> task_model.Done | None:
    result: Result = await db.execute(  # ✅ 비동기 실행
        select(task_model.Done).filter(task_model.Done.id == task_id)
    )
    return result.scalars().first()  # ✅ 결과 반환

async def create_done(db: AsyncSession, task_id: int) -> task_model.Done:
    done = task_model.Done(id=task_id)  # Done 객체 생성
    db.add(done)
    await db.commit()  # ✅ `await` 추가
    await db.refresh(done)  # ✅ `await` 추가
    return done

async def delete_done(db: AsyncSession, original: task_model.Done) -> None:
    await db.delete(original)  # ✅ `await` 추가
    await db.commit()  # ✅ `await` 추가
