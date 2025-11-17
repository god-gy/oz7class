### 유저 생성 API 작성하기

# - **요구사항**
# 클라이언트가 **username, age, gender**를 **Request Body**로 전달하면,
# 1. **Pydantic 모델을 활용하여 데이터 유효성을 검증**하고,
# 2. 검증된 데이터를 사용하여 **UserModel의 인스턴스를 생성**한 뒤,
# 3. 생성된 유저의 **id**를 ****반환하는 **API 라우터 함수**를 작성하세요.

# - **조건**
# 1. FastAPI의 **Pydantic 모델**을 활용하여 **데이터 검증**을 수행해야 합니다.
# 2. **username**은 **문자열(str), age**는 **정수(int), gender** 는
# **Enum** 이며 **‘male’, ‘female’** 중에서만 **선택가능** 해야합니다.

from enum import Enum
from pydantic import BaseModel

class GenderEnum(str, Enum):
    male = 'male'
    female = 'female'

class UserCreateRequest(BaseModel):
    username: str
    age: int
    gender: GenderEnum

class UserUpdateRequest(BaseModel):
    username: str | None = None
    age: int | None = None

class UserSearchParams(BaseModel):
    model_config = {"extra": "forbid"}

    username: str | None = None
    age: int | None = None
    gender: GenderEnum | None = None
