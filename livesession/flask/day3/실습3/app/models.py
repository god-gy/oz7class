''' db 모듈 '''
import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

#########
# DB 설정
#########

# /Users/admin/StudyClass/oz7class/livesession/flask/day3/실습2
BASE_DIR = os.path.dirname(__file__)

# /Users/admin/StudyClass/oz7class/livesession/flask/day3/실습2/instance
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")

# 없으면 폴더를 만들고 있으면 그걸 써라
os.makedirs(INSTANCE_DIR, exist_ok=True)

# /Users/admin/StudyClass/oz7class/livesession/flask/day3/실습2/instance/todos.db
DATABASE_URL = f'sqlite:///{os.path.join(INSTANCE_DIR, "todos.db")}'

engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False}   # 스레드 옵션
)

SessionLcal = sessionmaker(bind=engine)

#########
# 모델 정의
#########

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String(200), nullable=False)

    def __repr__(self):
        return f'<Todo id={self.id}, name="{self.name}")'

Base.metadata.create_all(bind=engine)
