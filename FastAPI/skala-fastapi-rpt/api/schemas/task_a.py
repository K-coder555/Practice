from typing import Optional  # Python 3.9 이하 버전 지원
from pydantic import BaseModel, Field, ConfigDict

class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="세탁소에 맡긴 것을 찾으러 가기")

    model_config = ConfigDict(from_attributes=True)

class TaskCreate(TaskBase):    
    pass

class TaskCreateResponse(TaskCreate): 
    id: int

    model_config = ConfigDict(from_attributes=True)

class Task(TaskBase):
    id: int
    done: bool = Field(False, description="완료 플래그")

    model_config = ConfigDict(from_attributes=True)
