from fastapi import APIRouter

from api.api_v1.endpoints import keys, languages, pages, projects, values

api_router = APIRouter()

api_router.include_router(keys.router, prefix="/keys", tags=["keys"])
api_router.include_router(languages.router, prefix="/languages", tags=["languages"])
api_router.include_router(pages.router, prefix="/pages", tags=["pages"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(values.router, prefix="/values", tags=["values"])

