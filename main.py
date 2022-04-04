from fastapi import FastAPI, Request

from core.config import Settings
from api.api_v1.api import api_router
from db.database import engine, Base

from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import JSONResponse

from schemas import RestfulErrorModel

Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=RestfulErrorModel(
            data='',
            errorCode=exc.status_code,
            errorMessage=exc.detail,
            showType='',
            traceId='',
            host=str(request.client.host) + ':' + str(request.client.port)
        ).dict(),
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content=RestfulErrorModel(
            data='',
            errorCode=400,
            errorMessage='Request Error',
            showType='',
            traceId='',
            host=str(request.client.host) + ':' + str(request.client.port)
        ).dict(),
    )


app.include_router(api_router, prefix=Settings().API_V1_STR)
