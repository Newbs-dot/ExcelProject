from sqlalchemy.orm import Session

from models import UserCheck, UserUpdateRole, User, UserCreate, role
from .base_repository import BaseRepository
from ..orms import UserOrm


class UsersRepository(BaseRepository):

    def is_user_exist(self, db: Session, check_user: UserCheck) -> bool:
        user = db.query(UserOrm).filter(UserOrm.telegram_id.contains(check_user.telegram_id)).first()
        db.close()

        return user is not None

    def create_user(self, db: Session, user_create: UserCreate) -> User | None:
        if self.is_user_exist(db, UserCheck(telegram_id=user_create.telegram_id)):
            return None

        user = UserOrm(telegram_id=user_create.telegram_id, role=role.User)
        db.add(user)
        db.commit()
        db.refresh(user)
        db.close()

        return user

    def update_user_role(self, db: Session, id: int, update_user: UserUpdateRole) -> User | None:
        user = self.get_by_id(db, id)

        if user is None:
            return user

        user.role = update_user.role
        db.commit()
        db.refresh(user)
        db.close()


users_repository = UsersRepository(UserOrm)
