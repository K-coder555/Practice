import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base

from api.models.task_a import Base  # ✅ 기존 `Base` 가져오기

# ✅ 비동기 MySQL 데이터베이스 URL
ASYNC_DB_URL = "mysql+aiomysql://manager:SqlDba-1@0.0.0.0:53303/demo?charset=utf8mb4"
# ASYNC_DB_URL = "mysql+aiomysql://root@db:3306/demo?charset=utf8mb4"

# ✅ 비동기 데이터베이스 엔진 생성
async_engine = create_async_engine(ASYNC_DB_URL, echo=True)

# ✅ ORM 모델을 비동기 지원 가능하도록 설정
# Base = declarative_base(cls=AsyncAttrs)  # ✅ AsyncAttrs 추가 > *중복 코드 삭제해 주기

# ✅ 비동기 데이터베이스 초기화 함수
async def reset_database():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)  # ✅ 테이블 삭제
        await conn.run_sync(Base.metadata.create_all)  # ✅ 테이블 생성
        
            # ✅ 이벤트 루프 종료 전에 데이터베이스 연결 정리
    await async_engine.dispose()

# ✅ 스크립트 실행 시 데이터베이스 초기화
if __name__ == "__main__":
    asyncio.run(reset_database())  # ✅ 비동기 실행
