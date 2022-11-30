from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db, users_repository
from sender.models import User, SuccessResponse, UserCreate, UserUpdateRole, role

router = APIRouter()


@router.get('/')
async def get_users(db: Session = Depends(get_db)) -> list[User]:
    return users_repository.get_users(db)


@router.get('/{telegramId}')
async def get_user(telegram_id: str, db: Session = Depends(get_db)) -> User | HTTPException:
    user = users_repository.get_user_by_id(db, telegram_id)
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')

    return user


@router.post('/')
async def create_user(user_create: UserCreate, db: Session = Depends(get_db)) -> SuccessResponse | HTTPException:
    user = users_repository.create_user(db, user_create)
    if user is None:
        raise HTTPException(status_code=404, detail='User is currently exist')

    return SuccessResponse()


@router.put('/{telegramId}')
async def update_user_role(telegram_id: str, user_update_role: UserUpdateRole, db: Session = Depends(get_db)) -> SuccessResponse | HTTPException:
    if user_update_role.role not in role.User and user_update_role.role not in role.Admin:
        raise HTTPException(status_code=404, detail='Invalid user role')
    user = users_repository.update_user_role(db, telegram_id, user_update_role.role)
    if user is None:
        raise HTTPException(status_code=404, detail='User is currently exist')

    return SuccessResponse()


@router.delete('/{telegramId}')
async def delete_user(telegram_id: str, db: Session = Depends(get_db)) -> SuccessResponse | HTTPException:
    user = users_repository.get_user_by_id(db, telegram_id)
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    users_repository.delete_user_by_id(db, telegram_id)

    return SuccessResponse()
