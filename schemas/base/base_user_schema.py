from pydantic import BaseModel, ConfigDict


class BaseUserSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str | None
    is_active: bool

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "phone": "+1234567890",
                "is_active": True,
            }
        }
    )
