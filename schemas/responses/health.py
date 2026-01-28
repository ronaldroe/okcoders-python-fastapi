from pydantic import BaseModel, ConfigDict

from enums.health import HealthStatuses


class HealthSchema(BaseModel):
    name: str
    status: HealthStatuses = HealthStatuses.HEALTHY
    uptime: float
    version: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "User Microservice",
                "status": "healthy",
                "uptime": 12345.67,
                "version": "0.1.0",
            }
        }
    )
