from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from schemas.responses.user_response_schema import UserResponseSchema


class UserService:
    @staticmethod
    def get_user(user_id: int) -> JSONResponse:
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
