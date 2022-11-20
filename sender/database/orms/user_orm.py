from sqlalchemy import Column, String, Integer

from ..database import Base


class UserOrm(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(String, unique=True, index=True)
    role = Column(String)

    class Config:
        orm_mode = True
