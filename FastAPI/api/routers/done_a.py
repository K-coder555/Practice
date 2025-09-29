from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Dict
import api.schemas.done_a as done_schema
import api.cruds.done_a as done_crud
from api.db_a import get_db
router = APIRouter()
@router.put("/tasks/{task_id}/done", response_model=done_schema.DoneResponse)
async def mark_task_as_done(task_id: int, db: AsyncSession = Depends(get_db)):
    """
    특정 task를 완료로 표시
    """
    # 이미 완료 상태인지 확인
    done = await done_crud.get_done(db, task_id=task_id)
    if done is not None:
        raise HTTPException(status_code=400, detail="Task is already marked as done.")
    # 완료 처리
    await done_crud.create_done(db, task_id)
    return done_schema.DoneResponse(id=task_id)  # :흰색_확인_표시: done 필드 필요 없음
@router.delete("/tasks/{task_id}/done", response_model=Dict[str, str])
async def unmark_task_as_done(task_id: int, db: AsyncSession = Depends(get_db)):
    """
    특정 task의 완료 상태 해제
    """
    done = await done_crud.get_done(db, task_id=task_id)
    if done is None:
        raise HTTPException(status_code=404, detail="Task is not marked as done.")
    await done_crud.delete_done(db, original=done)
    return {"detail": f"Task {task_id} has been marked as not done."}