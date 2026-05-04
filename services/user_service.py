from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from repositories.user_repository import UserRepository
from schemas.base.base_user_schema import BaseUserSchema
from schemas.responses.user_response_schema import UserResponseSchema


class UserService:
    @staticmethod
    def get_user(user_id: str) -> JSONResponse:
        user_data: UserResponseSchema = UserRepository.get_user_by_id(user_id)

        return JSONResponse(
            status_code=200,
            content=jsonable_encoder(user_data),
        )

    @staticmethod
    def create_user(user: BaseUserSchema) -> JSONResponse:
        user_data: UserResponseSchema = UserRepository.create_user(user)

        return JSONResponse(
            status_code=201,
            content=jsonable_encoder(user_data),
        )
