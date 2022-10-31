from fastapi import FastAPI

app = FastAPI(
    title='aue',
    openapi_url=f'/v1/openapi.json',
)

 
@app.get("/")
def read_root():
    return {"Hello": "World"}
