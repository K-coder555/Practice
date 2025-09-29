from pydantic import BaseModel, Field

class TaskBase(BaseModel):   # TaskBase를 정의합니다.
     title: str | None = Field(None, example="세탁소에 맡긴 것을 찾으러 가기")
     
class TaskCreate(TaskBase): 
    pass         # TaskBase를 상속받음 → 추가적인 필드 없이 그대로 사용 가능하며, title 필드만 포함됨

class TaskCreateResponse(TaskCreate): 
    id: int

    class Config:
        orm_mode = True        
             
class Task(TaskBase):   # 할일 데이터를 조회할 때 사용하는 모델, TaskBase를 상속받아 title 필드를 포함
    id: int
    done: bool = Field(False, description="완료 플래그")

    class Config:
        orm_mode = True