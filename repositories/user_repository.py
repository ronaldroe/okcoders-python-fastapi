from schemas.base.base_user_schema import BaseUserSchema
from schemas.responses.user_response_schema import UserResponseSchema

class UserRepository:
    @staticmethod
    def get_user(user_id: str) -> UserResponseSchema:
        return UserResponseSchema(
            id=user_id,
            first_name="John",
            last_name="Doe",
            email="john.doe@alchemer.com",
            phone="+1234567890",
            is_active=True,
        )

    @staticmethod
    def create_user(user: BaseUserSchema) -> UserResponseSchema:
        return UserResponseSchema(
            id="123e4567-e89b-12d3-a456-426614174000",
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            phone=user.phone,
            is_active=user.is_active,
        )
