from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

from schemas.base.base_user_schema import BaseUserSchema
from schemas.responses.user_response_schema import UserResponseSchema

user_router = APIRouter()


@user_router.get(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserResponseSchema,
)
def get_user(user_id: str) -> JSONResponse:
    return UserResponseSchema(
        id=user_id,
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        phone="+1234567890",
        is_active=True,
    )


@user_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponseSchema,
)
def create_user(request: Request, user: BaseUserSchema) -> JSONResponse:
    return UserResponseSchema(
        id="new_user_id",
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        phone=user.phone,
        is_active=True,
    )
