from typing import Optional

from sqlalchemy.orm import Session

from sender.models import User, UserCreate, role, Config
from ..orms import UserOrm, ConfigOrm


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
        user = cls.get_user_by_id(db, telegram_id)
        obj = db.query(UserOrm).get(user.id)
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

    @classmethod
    def create_user_config(cls, db: Session, url: str, file: str, telegram_id: str) -> Config:
        db_config = ConfigOrm(file=file, name=url, telegram_id=telegram_id)
        db.add(db_config)
        db.commit()
        db.refresh(db_config)
        db.close()

        return db_config


users_repository = UsersRepository()
