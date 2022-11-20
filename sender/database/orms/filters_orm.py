from sqlalchemy import Column, String, Integer

from ..database import Base


class FilterOrm(Base):
    __tablename__ = "filters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    class Config:
        orm_mode = True
