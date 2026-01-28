from uuid import uuid4
from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from schemas.responses.user_response_schema import UserResponseSchema

user_router = APIRouter()


@user_router.get("/{user_id}", status_code=status.HTTP_200_OK)
def get_user(user_id: int):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(
            UserResponseSchema(
                id=uuid4(),
                first_name="John",
                last_name="Doe",
                email="john.doe@example.com",
                phone="+1234567890",
                is_active=True,
            )
        ),
    )
