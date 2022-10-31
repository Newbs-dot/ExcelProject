from fastapi import APIRouter

router = APIRouter()


@router.post("/google_doc/check")
def check_url(url):
    return {"Hello": "World"}


@router.post("/google_doc/write")
def write_data():
    return {"Hello": "World"}
