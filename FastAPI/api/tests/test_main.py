import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from api.db_a import get_db, Base
from api.main import app
import starlette.status


ASYNC_DB_URL = "sqlite+aiosqlite:///./test.db"


@pytest_asyncio.fixture(scope="function")
async def async_client() -> AsyncClient:
    """ 비동기 테스트 클라이언트 생성 및 DB 초기화 """
    async_engine = create_async_engine(ASYNC_DB_URL, echo=True, future=True)
    async_session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )

    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async def get_test_db():
        async with async_session() as session:
            yield session

    app.dependency_overrides[get_db] = get_test_db

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:
        yield client

@pytest.mark.asyncio
async def test_create_and_read(async_client):
    """ 테스크 생성 및 조회 테스트 """
    response = await async_client.post("/tasks", json={"title": "테스트작업"})
    assert response.status_code == starlette.status.HTTP_200_OK
    response_obj = response.json()
    assert response_obj.get("title") == "테스트작업"
    response = await async_client.get("/tasks")
    assert response.status_code == starlette.status.HTTP_200_OK
    response_obj = response.json()
    assert len(response_obj) == 1
    assert response_obj[0].get("title") == "테스트작업"
    assert response_obj[0].get("done") is False
    
@pytest.mark.asyncio
async def test_done_flag(async_client):
    """ 완료 플래그 테스트 """
    # 작업 생성
    response = await async_client.post("/tasks", json={"title": "테스트 작업2"})
    assert response.status_code == starlette.status.HTTP_200_OK
    response_obj = response.json()
    assert response_obj.get("title") == "테스트 작업2"
    # 작업 목록 조회
    response = await async_client.get("/tasks")
    tasks = response.json()
    assert tasks, "No tasks found in database"
    task_id = tasks[0]["id"]
    # 완료 처리
    response = await async_client.put(f"/tasks/{task_id}/done")
    assert response.status_code == starlette.status.HTTP_200_OK
    response_obj = response.json()
    assert response_obj.get("id") == task_id, "Task ID should match"
    # 목록 재조회로 done 여부 확인
    response = await async_client.get("/tasks")
    tasks = response.json()
    updated_task = next((task for task in tasks if task["id"] == task_id), None)
    assert updated_task is not None, "Updated task not found"
    assert updated_task.get("done") is True, "Task should be marked as done"