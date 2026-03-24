from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from schemas.base.base_user_schema import BaseUserSchema
from schemas.responses.user_response_schema import UserResponseSchema


class UserService:
    @staticmethod
    def get_user(user_id: str) -> JSONResponse:
        user_data = {
            "id": user_id,
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "+1234567890",
            "is_active": True,
        }

        return JSONResponse(
            status_code=200,
            content=jsonable_encoder(UserResponseSchema(**user_data)),
        )

    @staticmethod
    def create_user(user: BaseUserSchema) -> JSONResponse:
        user_data = {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone": user.phone,
            "is_active": user.is_active,
        }

        return JSONResponse(
            status_code=201,
            content=jsonable_encoder(UserResponseSchema(**user_data)),
        )
