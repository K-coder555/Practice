from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
# from api.routers import task_a
# from api.routers import done_a
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.openapi.docs import get_swagger_ui_html
#import os
# import sys, os
# sys.path.append(os.path.dirname("C:\workspace\demo-app\api\rag.py"))
from rag import vector_retriever
from rag import bm25_retriever
from rag import ensemble_retriever
from rag import run_chain_hyde_rerank
# FastAPI 엔드포인트 정의 이해
# FastAPI는 아래 두 가지 방식 중 하나로 엔드포인트를 정의
# ① 직접 app에 정의
# ② 모듈화한 라우터 파일을 include

# app = FastAPI()
# FastAPI 앱(서버)의 기본 뼈대 생성
app = FastAPI(docs_url=None)

# 요청·응답 모델
class AskRequest(BaseModel):
    question: str
    retriever: str = "ensemble"  # ensemble | vector | bm25

class AskResponse(BaseModel):
    answer: str
    retriever: str

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI server!"}

@app.get("/health")
async def health():
    return {"status": "ok"}
# ① 경로 (/) 및 (/hello)에 대한 라우팅 추가 (라우터 파일 내에서 경로를 직접 정의)
# 별도의 라우팅이 없으면 GET /tasks, POST /tasks 등의 API가 동작하지 않음

# app.include_router(task.router)를 호출해야 task.py의 엔드포인트가 FastAPI 앱에 등록
# 여러 개의 라우트 모듈을 관리하기 쉽게 하기 위해 include_router()를 사용

# ② 라우터 등록 (FastAPI 앱에 실제로 등록, 모듈화한 라우터 파일을 include)
# app.include_router(task_a.router) # main.py에서 api/routers/task.py의 라우트를 include_router()로 FastAPI 앱에 추가
# app.include_router(done_a.router) # main.py에서 api/routers/done.py의 라우트를 include_router()로 FastAPI 앱에 추가

# static 경로 mount (필수!)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")  # 현재 main.py가 api/ 안에 있다고 가정
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# favicon 직접 연결
@app.get("/favicon.ico")
async def favicon():
    return FileResponse(os.path.join(STATIC_DIR, "favicon.ico"))

# Swagger UI 커스터마이징 - favicon 적용
from fastapi.openapi.docs import get_swagger_ui_html

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="My API Docs",
        swagger_favicon_url="/static/favicon.ico"
    )

@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    rtype = req.retriever.lower()
    if rtype == "ensemble":
        r = ensemble_retriever
    elif rtype == "vector":
        r = vector_retriever
    elif rtype == "bm25":
        r = bm25_retriever
    else:
        raise HTTPException(status_code=400, detail="retriever must be one of: ensemble, vector, bm25")

    try:
        answer = run_chain_hyde_rerank(r, req.question)
        return AskResponse(answer=answer, retriever=rtype)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# uvicorn api.main:app --host 127.0.0.1 -port 8003 --reload