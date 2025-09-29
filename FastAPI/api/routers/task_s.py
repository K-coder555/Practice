from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from api.db_s import get_db

import api.cruds.task_s as task_crud
import api.schemas.task_s as task_schema

router = APIRouter()

@router.get("/tasks", response_model=list[task_schema.Task])
def list_tasks(db: Session = Depends(get_db)): 
    return task_crud.get_tasks_with_done(db)
# async def list_tasks():
#    return [task_schema.Task(id=1, title="첫번째 ToDo 작업")]

@router.post("/tasks",  response_model=task_schema.TaskCreateResponse) 
def create_task(task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=1, **task_body.dict()) 
# task_body.dict()의 결과는 { "title": ＂세탁소에 맡긴 것을 찾으러 가기" } 형태의 딕셔너리이며 
# **task_body.dict()는 이 딕셔너리의 키-값 쌍을 함수 호출 시 개별 인수로 전달합니다.

@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreate) 
def update_task(task_id: int, task_body: task_schema.TaskCreate): 
    return task_schema.TaskCreateResponse(id=task_id, **task_body.dic())

@router.delete("/tasks/{task_id}") 
def delete_task(task_id: int):
    return
