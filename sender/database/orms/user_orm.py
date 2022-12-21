from sqlalchemy import Column, String, Integer, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship

from ..database import Base


class UserOrm(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(String, unique=True, index=True)
    role = Column(String)

    configs = relationship("ConfigOrm", backref="users")

    class Config:
        orm_mode = True


class ConfigOrm(Base):
    __tablename__ = "configs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    file = Column(String)
    telegram_id = Column(String, ForeignKey("users.telegram_id"))

    owner = relationship("UserOrm", back_populates="configs")

    class Config:
        orm_mode = True
