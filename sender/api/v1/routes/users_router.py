from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db, users_repository
from models import User, SuccessResponse, UserCreate, UserUpdateRole, role, UserCheck, IsUserCreate

router = APIRouter()


@router.get('/', response_model=list[User])
async def get_users(db: Session = Depends(get_db)) -> list[User]:
    return users_repository.get_items(db)


@router.get('/{id}', response_model=User)
async def get_user(id: int, db: Session = Depends(get_db)) -> User:
    user = users_repository.get_by_id(db, id)
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')

    return user


@router.post('/check', response_model=IsUserCreate)
async def check_is_user_create(user_check: UserCheck, db: Session = Depends(get_db)) -> IsUserCreate:
    is_user_exist = users_repository.is_user_exist(db, user_check)

    return IsUserCreate(is_user_exist=is_user_exist)


@router.post('/', response_model=SuccessResponse)
async def create_user(user_create: UserCreate, db: Session = Depends(get_db)) -> SuccessResponse:
    user = users_repository.create_user(db, user_create)
    if user is None:
        raise HTTPException(status_code=404, detail='User is currently exist')

    return SuccessResponse()


@router.put('/{id}', response_model=SuccessResponse)
async def update_user_role(id: int, user_update_role: UserUpdateRole, db: Session = Depends(get_db)) -> SuccessResponse:
    if user_update_role.role is not role.User and user_update_role.role is not role.Admin:
        raise HTTPException(status_code=404, detail='Invalid user role')
    user = users_repository.update_user_role(db, id, user_update_role)
    if user is None:
        raise HTTPException(status_code=404, detail='User is currently exist')

    return SuccessResponse()


@router.delete('/{id}', response_model=SuccessResponse)
async def delete_user(id: int, db: Session = Depends(get_db)) -> SuccessResponse:
    user = users_repository.get_by_id(db, id)
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    users_repository.delete_by_id(db, id)

    return SuccessResponse()
