from typing import Optional

from sqlalchemy.orm import Session

from sender.models import User, UserCreate, role
from ..orms import UserOrm


class UsersRepository:
    @classmethod
    def get_user_by_id(cls, db: Session, telegram_id: str) -> Optional[User]:
        item = db.query(UserOrm).filter(UserOrm.telegram_id == telegram_id).first()
        db.close()

        return item

    @classmethod
    def get_users(cls, db: Session) -> list[User]:
        items = db.query(UserOrm).all()
        db.close()

        return items

    @classmethod
    def delete_user_by_id(cls, db: Session, telegram_id: str) -> None:
        obj = db.query(UserOrm).get(telegram_id)
        db.delete(obj)
        db.commit()
        db.close()

    @classmethod
    def create_user(cls, db: Session, user_create: UserCreate) -> User | None:
        if cls.get_user_by_id(db, user_create.telegram_id):
            return None

        user = UserOrm(telegram_id=user_create.telegram_id, role=role.User)
        db.add(user)
        db.commit()
        db.refresh(user)
        db.close()

        return user

    @classmethod
    def update_user_role(cls, db: Session, telegram_id: str, role: str) -> User | None:
        user = db.query(UserOrm).filter(UserOrm.telegram_id == telegram_id).update({'role': role})

        db.commit()
        db.close()

        return user


users_repository = UsersRepository()
