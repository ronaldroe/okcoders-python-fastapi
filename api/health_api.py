import os
from time import time

from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from schemas.responses.health import HealthSchema
from enums.health import HealthStatuses

health_router = APIRouter()
start_time = time()


@health_router.get("/", status_code=status.HTTP_200_OK, response_model=HealthSchema)
def health_check():
    current_time = time()
    uptime = current_time - start_time

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(
            HealthSchema(
                name=f"{os.environ.get('SERVICE_NAME', 'User')} Microservice",
                status=HealthStatuses.HEALTHY,
                uptime=uptime,
                version=os.environ.get("VERSION", "0.1.0"),
            )
        ),
    )
