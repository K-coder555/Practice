from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="세탁소에 맡긴 것을 찾으러 가기")
    model_config = ConfigDict(from_attributes=True)
class TaskCreate(TaskBase):
    pass
class TaskCreateResponse(TaskCreate):
    id: int
    done: bool  # :흰색_확인_표시: dones 테이블 기준으로 수동 주입됨
    model_config = ConfigDict(from_attributes=True)
class Task(TaskBase):
    id: int
    done: bool = Field(..., description="완료 플래그")  # :흰색_확인_표시: 반드시 클라이언트에 포함되어야 함
    model_config = ConfigDict(from_attributes=True)
