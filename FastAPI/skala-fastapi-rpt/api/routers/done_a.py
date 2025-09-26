from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

import api.schemas.done_a as done_schema 
import api.cruds.done_a as done_crud 
from api.db_a import get_db

router = APIRouter()

@router.put("/tasks/{task_id}/done", response_model=done_schema.DoneResponse)
async def mark_task_as_done(task_id: int, db: Session = Depends(get_db)):
    done = await done_crud.get_done(db, task_id=task_id) # 비동기 함수 앞에 await 추가
    if done is not None:
         raise HTTPException(status_code=400, detail="Done already exits")
    return await done_crud.create_done(db, task_id) # 비동기 함수 앞에 await 추가

@router.delete("/tasks/{task_id}/done",  response_model=None)
async def unmark_task_as_done(task_id: int, db: Session = Depends(get_db)) :
    done = await done_crud.get_done(db, task_id=task_id) # 비동기 함수 앞에 await 추가
    if done is None:
         raise HTTPException(status_code=404, detail="Done not found")
    return await done_crud.delete_done(db, original=done) # 비동기 함수 앞에 await 추가
