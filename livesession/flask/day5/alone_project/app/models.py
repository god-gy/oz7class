''' DB 모델 정의 (Review 모델) '''
import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

BASE_DIR = os.path.dirname(__file__)
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
os.makedirs(INSTANCE_DIR, exist_ok=True)
DATABASE_URL = f'sqlite:///{os.path.join(INSTANCE_DIR, "reviews.db")}'

engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False}
)

SessionLcal = sessionmaker(bind=engine)

Base = declarative_base()

class Review(Base):
    __tablename__ = 'reivews'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(200), nullable=False)

    def __repr__(self):
        return f'<review id={self.id}, content="{self.content}")'

Base.metadata.create_all(bind=engine)
