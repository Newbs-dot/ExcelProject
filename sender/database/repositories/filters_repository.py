from sqlalchemy.orm import Session

from models import FilterCreate, Filter
from services import filter_service
from .base_repository import BaseRepository
from ..orms import FilterOrm


class FiltersRepository(BaseRepository):
    def create_filter(self, db: Session, filter_create: FilterCreate) -> Filter | None:
        filters = self.get_items(db)

        if filter_service.can_create_filter(filter_create.name, filters):
            filter = FilterOrm(name=filter_create.name)
            db.add(filter)
            db.commit()
            db.refresh(filter)
            db.close()

            return filter

        return None


filters_repository = FiltersRepository(FilterOrm)
