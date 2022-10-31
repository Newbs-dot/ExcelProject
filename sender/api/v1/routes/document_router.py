from fastapi import APIRouter

router = APIRouter()


@router.post("/document/check")
def check_document():
    return {"Hello": "World"}


@router.get("/document/get/data")
def get_data():
    return {"Hello": "World"}
