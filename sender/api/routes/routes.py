from fastapi import APIRouter

router = APIRouter()

@app.get("/")
def read_root():
    return {"Hello": "World"}