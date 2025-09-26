from sqlalchemy import create_engine

from api.models.task_s import Base

DB_URL  =  "mysql+pymysql://root@db:3306/demo?charset=utf8" # 로컬에서 컨테이너 DB에 접속 시
# DB_URL = "mysql+pymysql://manager:SqlDba-1@172.18.0.2:53301/demo?charset=utf8mb4"

engine = create_engine(DB_URL, echo=True)

def reset_database():
  Base.metadata.drop_all(bind=engine) 
  Base.metadata.create_all(bind=engine)

if __name__== "__main__":
    reset_database()

