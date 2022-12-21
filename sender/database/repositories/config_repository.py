from typing import Optional

from sqlalchemy.orm import Session

from ..orms import ConfigOrm


class ConfigsRepository:
    @classmethod
    def get_config_by_id(cls, db: Session, url: str) -> Optional[ConfigOrm]:
        test = db.query(ConfigOrm).all()
        db.close()
        for x in test:
            if x.name in url:
                return x

        return None


configs_repository = ConfigsRepository()
