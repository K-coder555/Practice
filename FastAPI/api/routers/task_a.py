from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import api.cruds.task_a as task_crud
import api.cruds.done_a as done_crud  # :흰색_확인_표시: 이 줄 추가!!
from api.db_a import get_db
import api.schemas.task_a as task_schema

router = APIRouter()

@router.get("/tasks", response_model=list[task_schema.Task])
async def list_tasks(db: AsyncSession = Depends(get_db)):
    return await task_crud.get_tasks_with_done(db)
@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)):
    task = await task_crud.create_task(db, task_body)
    return task_schema.TaskCreateResponse(
        id=task.id,
        title=task.title,
        done=False  # :흰색_확인_표시: 새로 만든 task는 기본적으로 done이 아님
    )
@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(task_id: int, task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)):
    task = await task_crud.get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    updated_task = await task_crud.update_task(db, task_body, original=task)
    # :흰색_확인_표시: get_done은 done_crud에서 호출해야 함
    done = await done_crud.get_done(db, task_id=task_id)
    return task_schema.TaskCreateResponse(
        id=updated_task.id,
        title=updated_task.title,
        done=done is not None
    )
@router.delete("/tasks/{task_id}", response_model=dict)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    # 1. 삭제 대상 task 조회
    task = await task_crud.get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    # 2. 해당 task의 done 여부 확인 후 삭제
    done = await done_crud.get_done(db, task_id=task_id)
    if done is not None:
        await done_crud.delete_done(db, original=done)
    # 3. 실제 task 삭제
    await task_crud.delete_task(db, original=task)
    return {"message": f"Task {task_id} deleted successfully"}