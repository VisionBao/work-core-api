from fastapi import FastAPI

from core.config import Settings
from api.api_v1.api import api_router
from db.database import engine, Base


Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(api_router, prefix=Settings().API_V1_STR)
