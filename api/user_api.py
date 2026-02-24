from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from services.user_service import UserService

user_router = APIRouter()


@user_router.get("/{user_id}", status_code=status.HTTP_200_OK)
def get_user(user_id: int) -> JSONResponse:
    return UserService.get_user(user_id)
