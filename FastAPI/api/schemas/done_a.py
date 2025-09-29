from pydantic import BaseModel, ConfigDict
class DoneResponse(BaseModel):
    id: int
    # done: bool -> 해당 테이블에 id 값 존재 여부로 판단하므로 done 컬럼은 불필요
    # model_config = ConfigDict(from_attributes=True)