from typing import Annotated
from datetime import datetime

from fastapi import Path, HTTPException, Query, APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from ..models.movies import MovieModel
from ..schemas.movies import MovieResponse, CreateMovieRequest, MovieSearchParams, MovieUpdateRequest
from ..schemas.users import Token
from ..models.users import UserModel
from ..routers.users import user_router

movie_router = APIRouter(prefix="/movies", tags=["movies"])

@movie_router.post('', response_model=MovieResponse, status_code=201)
async def create_movie(data: CreateMovieRequest):
    movie = MovieModel.create(**data.model_dump())
    return movie


@movie_router.get('', response_model=list[MovieResponse], status_code=200)
async def get_movies(query_params: Annotated[MovieSearchParams, Query()]):
    valid_query = {key: value for key, value in query_params.model_dump().items() if value is not None}

    if valid_query:
        return MovieModel.filter(**valid_query)

    return MovieModel.all()


@movie_router.get('/{movie_id}', response_model=MovieResponse, status_code=200)
async def get_movie(movie_id: int = Path(gt=0)):
    movie = MovieModel.get(id=movie_id)
    if movie is None:
        raise HTTPException(status_code=404)
    return movie


@movie_router.patch('/{movie_id}', response_model=MovieResponse, status_code=200)
async def edit_movie(data: MovieUpdateRequest, movie_id: int = Path(gt=0)):
    movie = MovieModel.get(id=movie_id)
    if movie is None:
        raise HTTPException(status_code=404)
    movie.update(**data.model_dump())
    return movie


@movie_router.delete('/{movie_id}', status_code=204)
async def delete_movie(movie_id: int = Path(gt=0)):
    movie = MovieModel.get(id=movie_id)
    if movie is None:
        raise HTTPException(status_code=404)
    movie.delete()
    return

@user_router.post('/login', response_model=Token)
async def login_user(data: Annotated[OAuth2PasswordRequestForm, Depends()], create_access_token=None, status=None):
	user = UserModel.authenticate(data.username, data.password)
	if not user:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Incorrect username or password",
			headers={"WWW-Authenticate": "Bearer"},
		)
	access_token = create_access_token(data={"user_id": user.id})
	user.update(last_login=datetime.now())
	return Token(access_token=access_token, token_type="bearer")
