phoenix@Phoenix-MacBook-Pro api % docker compose exec demo-app poetry run pytest
/src/.venv/lib/python3.11/site-packages/pytest_asyncio/plugin.py:207: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
========================================================== test session starts ==========================================================
platform linux -- Python 3.11.4, pytest-8.3.4, pluggy-1.5.0
rootdir: /src
configfile: pyproject.toml
plugins: asyncio-0.25.3, anyio-4.8.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None
collected 2 items                                                                                                                       

api/tests/test_main.py .F                                                                                                         [100%]

=============================================================== FAILURES ================================================================
____________________________________________________________ test_done_flag _____________________________________________________________

async_client = <httpx.AsyncClient object at 0xffff86a8eb10>

    @pytest.mark.asyncio
    async def test_done_flag(async_client):
        """ 완료 플래그 테스트 """
        response = await async_client.post("/tasks", json={"title": "테스트 작업2"})
        assert response.status_code == starlette.status.HTTP_200_OK
        response_obj = response.json()
        assert response_obj.get("title") == "테스트 작업2"
    
        response = await async_client.get("/tasks")
        tasks = response.json()
        assert tasks, "No tasks found in database"
    
        task_id = tasks[0]["id"]
    
        response = await async_client.put(f"/tasks/{task_id}/done")
>       assert response.status_code == starlette.status.HTTP_200_OK
E       AssertionError: assert 400 == 200
E        +  where 400 = <Response [400 Bad Request]>.status_code
E        +  and   200 = <module 'starlette.status' from '/src/.venv/lib/python3.11/site-packages/starlette/status.py'>.HTTP_200_OK
E        +    where <module 'starlette.status' from '/src/.venv/lib/python3.11/site-packages/starlette/status.py'> = starlette.status

api/tests/test_main.py:69: AssertionError
--------------------------------------------------------- Captured stdout setup ---------------------------------------------------------
2025-02-26 07:38:19,013 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-02-26 07:38:19,013 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("tasks")
2025-02-26 07:38:19,013 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-02-26 07:38:19,014 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("dones")
2025-02-26 07:38:19,014 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-02-26 07:38:19,014 INFO sqlalchemy.engine.Engine 
DROP TABLE dones
2025-02-26 07:38:19,014 INFO sqlalchemy.engine.Engine [no key 0.00005s] ()
2025-02-26 07:38:19,016 INFO sqlalchemy.engine.Engine 
DROP TABLE tasks
2025-02-26 07:38:19,016 INFO sqlalchemy.engine.Engine [no key 0.00004s] ()
2025-02-26 07:38:19,019 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("tasks")
2025-02-26 07:38:19,019 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-02-26 07:38:19,019 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("tasks")
2025-02-26 07:38:19,019 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-02-26 07:38:19,019 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("dones")
2025-02-26 07:38:19,019 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-02-26 07:38:19,020 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("dones")
2025-02-26 07:38:19,020 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-02-26 07:38:19,020 INFO sqlalchemy.engine.Engine 
CREATE TABLE tasks (
        id INTEGER NOT NULL, 
        title VARCHAR(1024), 
        PRIMARY KEY (id)
)


2025-02-26 07:38:19,020 INFO sqlalchemy.engine.Engine [no key 0.00004s] ()
2025-02-26 07:38:19,022 INFO sqlalchemy.engine.Engine 
CREATE TABLE dones (
        id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(id) REFERENCES tasks (id)
)


2025-02-26 07:38:19,022 INFO sqlalchemy.engine.Engine [no key 0.00005s] ()
2025-02-26 07:38:19,025 INFO sqlalchemy.engine.Engine COMMIT
---------------------------------------------------------- Captured log setup -----------------------------------------------------------
INFO     sqlalchemy.engine.Engine:base.py:2699 BEGIN (implicit)
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA main.table_info("tasks")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA main.table_info("dones")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 
DROP TABLE dones
INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00005s] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 
DROP TABLE tasks
INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00004s] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA main.table_info("tasks")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA temp.table_info("tasks")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA main.table_info("dones")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 PRAGMA temp.table_info("dones")
INFO     sqlalchemy.engine.Engine:base.py:1843 [raw sql] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 
CREATE TABLE tasks (
        id INTEGER NOT NULL, 
        title VARCHAR(1024), 
        PRIMARY KEY (id)
)


INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00004s] ()
INFO     sqlalchemy.engine.Engine:base.py:1843 
CREATE TABLE dones (
        id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(id) REFERENCES tasks (id)
)


INFO     sqlalchemy.engine.Engine:base.py:1843 [no key 0.00005s] ()
INFO     sqlalchemy.engine.Engine:base.py:2705 COMMIT
--------------------------------------------------------- Captured stdout call ----------------------------------------------------------
2025-02-26 07:38:19,026 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-02-26 07:38:19,026 INFO sqlalchemy.engine.Engine INSERT INTO tasks (title) VALUES (?)
2025-02-26 07:38:19,026 INFO sqlalchemy.engine.Engine [generated in 0.00007s] ('테스트 작업2',)
2025-02-26 07:38:19,027 INFO sqlalchemy.engine.Engine COMMIT
2025-02-26 07:38:19,029 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-02-26 07:38:19,029 INFO sqlalchemy.engine.Engine SELECT tasks.id, tasks.title 
FROM tasks 
WHERE tasks.id = ?
2025-02-26 07:38:19,029 INFO sqlalchemy.engine.Engine [generated in 0.00008s] (1,)
2025-02-26 07:38:19,030 INFO sqlalchemy.engine.Engine SELECT dones.id AS dones_id 
FROM dones 
WHERE ? = dones.id
2025-02-26 07:38:19,030 INFO sqlalchemy.engine.Engine [generated in 0.00008s] (1,)
2025-02-26 07:38:19,031 INFO sqlalchemy.engine.Engine ROLLBACK
2025-02-26 07:38:19,031 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-02-26 07:38:19,032 INFO sqlalchemy.engine.Engine SELECT tasks.id, tasks.title, dones.id IS NOT NULL AS done 
FROM tasks LEFT OUTER JOIN dones ON tasks.id = dones.id
2025-02-26 07:38:19,032 INFO sqlalchemy.engine.Engine [generated in 0.00007s] ()
2025-02-26 07:38:19,032 INFO sqlalchemy.engine.Engine ROLLBACK
----------------------------------------------------------- Captured log call -----------------------------------------------------------
INFO     sqlalchemy.engine.Engine:base.py:2699 BEGIN (implicit)
INFO     sqlalchemy.engine.Engine:base.py:1843 INSERT INTO tasks (title) VALUES (?)
INFO     sqlalchemy.engine.Engine:base.py:1843 [generated in 0.00007s] ('테스트 작업2',)
INFO     sqlalchemy.engine.Engine:base.py:2705 COMMIT
INFO     sqlalchemy.engine.Engine:base.py:2699 BEGIN (implicit)
INFO     sqlalchemy.engine.Engine:base.py:1843 SELECT tasks.id, tasks.title 
FROM tasks 
WHERE tasks.id = ?
INFO     sqlalchemy.engine.Engine:base.py:1843 [generated in 0.00008s] (1,)
INFO     sqlalchemy.engine.Engine:base.py:1843 SELECT dones.id AS dones_id 
FROM dones 
WHERE ? = dones.id
INFO     sqlalchemy.engine.Engine:base.py:1843 [generated in 0.00008s] (1,)
INFO     sqlalchemy.engine.Engine:base.py:2702 ROLLBACK
INFO     sqlalchemy.engine.Engine:base.py:2699 BEGIN (implicit)
INFO     sqlalchemy.engine.Engine:base.py:1843 SELECT tasks.id, tasks.title, dones.id IS NOT NULL AS done 
FROM tasks LEFT OUTER JOIN dones ON tasks.id = dones.id
INFO     sqlalchemy.engine.Engine:base.py:1843 [generated in 0.00007s] ()
INFO     sqlalchemy.engine.Engine:base.py:2702 ROLLBACK
=========================================================== warnings summary ============================================================
api/db_a.py:20
  /src/api/db_a.py:20: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base(cls=AsyncAttrs)  # ✅ AsyncAttrs 추가

api/models/__init__.py:5
  /src/api/models/__init__.py:5: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

.venv/lib/python3.11/site-packages/pydantic/fields.py:1042
  /src/.venv/lib/python3.11/site-packages/pydantic/fields.py:1042: PydanticDeprecatedSince20: Using extra keyword arguments on `Field` is deprecated and will be removed. Use `json_schema_extra` instead. (Extra keys: 'example'). Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.10/migration/
    warn(

api/tests/test_main.py::test_done_flag
  /src/.venv/lib/python3.11/site-packages/starlette/_exception_handler.py:63: RuntimeWarning: coroutine 'get_done' was never awaited
    await response(scope, receive, sender)
  Enable tracemalloc to get traceback where the object was allocated.
  See https://docs.pytest.org/en/stable/how-to/capture-warnings.html#resource-warnings for more info.

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================== short test summary info ========================================================
FAILED api/tests/test_main.py::test_done_flag - AssertionError: assert 400 == 200
================================================ 1 failed, 1 passed, 4 warnings in 0.53s ================================================
phoenix@Phoenix-MacBook-Pro api % docker compose exec demo-app poetry run pytest