from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

from schemas.base.base_user_schema import BaseUserSchema
from schemas.responses.user_response_schema import UserResponseSchema
from services.user_service import UserService

user_router = APIRouter()


@user_router.get(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserResponseSchema,
)
def get_user(user_id: str) -> JSONResponse:
    return UserService.get_user(user_id)


@user_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponseSchema,
)
def create_user(request: Request, user: BaseUserSchema) -> JSONResponse:
    return UserService.create_user(user)
