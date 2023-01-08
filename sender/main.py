import uvicorn

from settings import settings

if __name__ == '__main__':
    uvicorn.run('app:app', port=settings.API_PORT, host=settings.API_HOST, reload=True)
