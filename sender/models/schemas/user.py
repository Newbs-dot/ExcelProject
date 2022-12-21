from pydantic import BaseModel

from .config import Config


class UserSchema(BaseModel):
    class Config:
        arbitrary_types_allowed = True


class User(UserSchema):
    id: int
    telegram_id: str
    role: str
    configs: list[Config] = []


class UserCheck(UserSchema):
    telegram_id: str


class UserUpdateRole(UserSchema):
    role: str


class UserCreate(UserSchema):
    telegram_id: str


class IsUserCreate(UserSchema):
    is_user_exist: bool
