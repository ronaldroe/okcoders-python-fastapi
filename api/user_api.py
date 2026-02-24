from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

from services.user_service import UserService

user_router = APIRouter()


@user_router.get("/{user_id}", status_code=status.HTTP_200_OK)
def get_user(user_id: int) -> JSONResponse:
    return UserService.get_user(user_id)


@user_router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(request: Request) -> JSONResponse:
    return UserService.create_user(request)
