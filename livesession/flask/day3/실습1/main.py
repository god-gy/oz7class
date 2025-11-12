from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 데이터베이스 연결
engine = create_engine("sqlite:///user.db", echo=True)

# Base 클래스 정의
Base = declarative_base()

# 모델(테이블) 정의
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    def __repr__(self): # 파이썬 객체를 개발자 친화적 문자열로 표현
        return f'<User(id={self.id}, name="{self.name}")'

# DB 안에 테이블 생성
Base.metadata.create_all(bind=engine)

# 세션 준비
SessionLcal = sessionmaker(bind=engine)

##### 단링 데이터 핸들링 #####
def run_single():
    db = SessionLcal()

    ############## Insert (생성)
    new_user = User(name='소민')
    db.add(new_user)
    db.commit()
    print("사용자 추가: ", new_user)

    ############## Select (조회)
    user = db.query(User).first()
    print("사용자 검색: ", user)

    ############## Update (수정)
    user = db.query(User).first()
    if user:
        user.name = '건우'
        db.commit()
        print("사용자 변경: ", user)

    ############## Delete (제거)
    user = db.query(User).first()
    if user:
        db.delete(user)
        db.commit()
        print("사용자 삭제: ", user)

    db.close()

##### 복수 데이터 핸들링 #####

db = SessionLcal()

############## Insert (여러 데이터 생성)
users = [User(name='BE_종찬'), User(name='BE_동석'), User(name='건영')]
db.add_all(users)
db.commit()
print("여러 사용자 추가: ", users)

############## Select

### 전체 데이터 검색
users = db.query(User).all()
for user in users:
    print("전체 데이터: ", user.name)

### 조건 검색
# 이름이 "건영"인 첫번째 사용자를 검색
find_user = db.query(User).filter(User.name == "건영").first()
print("조건 조회: ", find_user)
# 이름에 "BE_"가 포함된 사용자를 검색 (패턴 검색)
find_users = db.query(User).filter(User.name.like("BE_%")).all()
print("조건 조회: ", find_users)

############## Update (데이터 일괄 수정)
users = db.query(User).all()
for u in users:
    u.name = u.name + "_NEW"
db.commit()
print("업데이트 완료: ", users)

############## Delete
# 모든 데이터 제거
db.query(User).delete()
db.commit()
print("모든 유저 삭제 끝!!!")
users = db.query(User).all()
if users:
    print("아직 남았어: ", users)
else:
    print("데이터 모두 삭제 완료")

db.close()
