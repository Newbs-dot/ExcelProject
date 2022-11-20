from typing import Generic, Optional, TypeVar, Any

from sqlalchemy.orm import Session

TModel = TypeVar('TModel', bound=Any)


class BaseRepository(Generic[TModel]):
    def __init__(self, model: type[TModel]):
        self.model = model

    def get_by_id(self, db: Session, item_id: int) -> Optional[TModel]:
        item = db.query(self.model).filter(self.model.id == item_id).first()
        db.close()

        return item

    def get_items(self, db: Session) -> list[TModel]:
        items = db.query(self.model).all()
        db.close()

        return items

    def delete_by_id(self, db: Session, item_id: int) -> None:
        obj = db.query(self.model).get(item_id)
        db.delete(obj)
        db.commit()
        db.close()
