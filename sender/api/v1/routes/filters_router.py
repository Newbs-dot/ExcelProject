from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db, filters_repository
from models import Filter, SuccessResponse, FilterCreate

router = APIRouter()


@router.get('/', response_model=list[Filter])
async def get_filters(db: Session = Depends(get_db)) -> list[Filter]:
    return filters_repository.get_items(db)


@router.get('/{id}', response_model=Filter)
async def get_filter(id: int, db: Session = Depends(get_db)) -> Filter:
    filter = filters_repository.get_by_id(db, id)
    if filter is None:
        raise HTTPException(status_code=404, detail='Filter not found')

    return filter


@router.post('/', response_model=SuccessResponse)
async def create_filter(filter_create: FilterCreate, db: Session = Depends(get_db)) -> SuccessResponse:
    filter = filters_repository.create_filter(db, filter_create)
    if filter is None:
        raise HTTPException(status_code=404, detail='Filter is currently exist')

    return SuccessResponse()


@router.delete('/{id}', response_model=SuccessResponse)
async def delete_filter(id: int, db: Session = Depends(get_db)) -> SuccessResponse:
    filter = filters_repository.get_by_id(db, id)
    if filter is None:
        raise HTTPException(status_code=404, detail='Filter not found')
    filters_repository.delete_by_id(db, id)

    return SuccessResponse()
