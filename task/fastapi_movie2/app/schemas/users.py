from enum import Enum
from pydantic import BaseModel
from typing import Annotated

from fastapi import Depends, HTTPException

from ..models.users import UserModel
from ..routers.users import user_router
from ..utils.jwt import get_current_user

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

class Token(BaseModel):
    access_token: str
    token_type: str

@user_router.get('/me')
async def get_user(user: Annotated[UserModel, Depends(get_current_user)]):
	return user


@user_router.patch('/me')
async def update_user(
	user: Annotated[UserModel, Depends(get_current_user)],
	data: UserUpdateRequest,
):
	if user is None:
		raise HTTPException(status_code=404)
	user.update(**data.model_dump())
	return user


@user_router.delete('/me')
async def delete_user(user: Annotated[UserModel, Depends(get_current_user)]):
	user.delete()
	return {'detail': 'Successfully Deleted.'}