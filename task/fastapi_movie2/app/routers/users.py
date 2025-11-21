from typing import Annotated

from fastapi import Path, HTTPException, Query, APIRouter

from ..models.users import UserModel
from ..schemas.users import UserCreateRequest, UserUpdateRequest, UserSearchParams

user_router = APIRouter(prefix="/users", tags=["user"])

@user_router.post('')
async def create_user(data: UserCreateRequest):
    user = UserModel.create(**data.model_dump())
    return user.id


@user_router.get('')
async def get_all_users():
    result = UserModel.all()
    if not result:
        raise HTTPException(status_code=404)
    return result


@user_router.get('/search')
async def search_users(query_params: Annotated[UserSearchParams, Query()]):
    valid_query = {key: value for key, value in query_params.model_dump().items() if value is not None}
    filtered_users = UserModel.filter(**valid_query)
    if not filtered_users:
        raise HTTPException(status_code=404)
    return 	filtered_users


@user_router.get('/{user_id}')
async def get_user(user_id: int = Path(gt=0)):
    user = UserModel.get(id=user_id)
    if user is None:
        raise HTTPException(status_code=404)
    return user


@user_router.patch('/{user_id}')
async def update_user(data: UserUpdateRequest, user_id: int = Path(gt=0)):
    user = UserModel.get(id=user_id)
    if user is None:
        raise HTTPException(status_code=404)
    user.update(**data.model_dump())
    return user


@user_router.delete('/{user_id}')
async def delete_user(user_id: int = Path(gt=0)):
    user = UserModel.get(id=user_id)
    if user is None:
        raise HTTPException(status_code=404)
    user.delete()

    return {'detail': f'User: {user_id}, Successfully Deleted.'}