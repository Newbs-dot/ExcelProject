from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db, filters_repository
from models import SuccessResponse, FilterCreate, Filter

router = APIRouter()


@router.get('/')
async def get_filters(db: Session = Depends(get_db)) -> list[Filter]:
    return filters_repository.get_filters(db)


@router.get('/{id}')
async def get_filter(id: int, db: Session = Depends(get_db)) -> Filter | HTTPException:
    filter = filters_repository.get_filter_by_id(db, id)
    if filter is None:
        raise HTTPException(status_code=404, detail='Filter not found')

    return filter


@router.post('/')
async def create_filter(filter_create: FilterCreate, db: Session = Depends(get_db)) -> SuccessResponse | HTTPException:
    filter = filters_repository.create_filter(db, filter_create)
    if filter is None:
        raise HTTPException(status_code=404, detail='Filter is currently exist')

    return SuccessResponse()


@router.delete('/{id}')
async def delete_filter(id: int, db: Session = Depends(get_db)) -> SuccessResponse | HTTPException:
    filter = filters_repository.get_filter_by_id(db, id)
    if filter is None:
        raise HTTPException(status_code=404, detail='Filter not found')
    filters_repository.delete_filter_by_id(db, id)

    return SuccessResponse()
