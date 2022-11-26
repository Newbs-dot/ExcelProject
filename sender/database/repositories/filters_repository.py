from typing import Optional

from sqlalchemy.orm import Session

from models import FilterCreate, Filter
from services import filter_service
from ..orms import FilterOrm


class FiltersRepository:

    @classmethod
    def get_filter_by_id(cls, db: Session, item_id: int) -> Optional[Filter]:
        item = db.query(FilterOrm).filter(FilterOrm.id == item_id).first()
        db.close()

        return item

    @classmethod
    def get_filters(cls, db: Session) -> list[Filter]:
        items = db.query(FilterOrm).all()
        db.close()

        return items

    @classmethod
    def delete_filter_by_id(cls, db: Session, item_id: int) -> None:
        obj = db.query(FilterOrm).get(item_id)
        db.delete(obj)
        db.commit()
        db.close()

    @classmethod
    def create_filter(cls, db: Session, filter_create: FilterCreate) -> Filter | None:
        filters = cls.get_filters(db)

        if filter_service.can_create_filter(filter_create.name, filters):
            filter = FilterOrm(name=filter_create.name)
            db.add(filter)
            db.commit()
            db.refresh(filter)
            db.close()

            return filter

        return None


filters_repository = FiltersRepository()
