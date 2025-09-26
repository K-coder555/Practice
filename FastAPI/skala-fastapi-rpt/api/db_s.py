from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL  =  "mysql+pymysql://root@db:3306/demo?charset=utf8" # 로컬에서 컨테이너 DB에 접속 시

db_engine = create_engine(DB_URL, echo=True)
db_session = sessionmaker(
autocommit=False, autoflush=False, bind=db_engine
)

Base = declarative_base()

def get_db():
   db = SessionLocal() # 세션 인스턴스 생성
   try:
       yield db
   finally:
       db.close() # 요청이 끝난 후 세션 종료
