        
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncAttrs

# ✅ MySQL 비동기 데이터베이스 URL
# ASYNC_DB_URL = "mysql+aiomysql://manager@db:3306/demo?charset=utf8mb4"
ASYNC_DB_URL = "mysql+aiomysql://manager:SqlDba-1@127.0.0.1:53301/demo?charset=utf8mb4"

# ✅ 비동기 데이터베이스 엔진 생성
async_engine = create_async_engine(
    ASYNC_DB_URL,
    echo=True,
    future=True  # 최신 SQLAlchemy API 사용 시 권장
)

# ✅ 비동기 세션 팩토리 설정
AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,  # flush는 명시적으로
    autocommit=False  # commit은 명시적으로
)

# ✅ 비동기 지원을 위한 SQLAlchemy Base 클래스
Base = declarative_base(cls=AsyncAttrs)

# ✅ 비동기 데이터베이스 세션을 반환하는 종속성 함수 (트랜잭션 처리 포함)
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session  # 라우터에서 db 작업 수행
            await session.commit()  # ✅ 명시적 커밋
            print("[✅ COMMIT 완료]")
        except Exception as e:
            await session.rollback()  # ✅ 오류 발생 시 롤백
            print(f"[❌ ROLLBACK 발생]: {e}")
            raise
        finally:
            await session.close()
