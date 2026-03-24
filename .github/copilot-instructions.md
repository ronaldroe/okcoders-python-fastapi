# Copilot Instructions

## Project Overview

OK Coders FastAPI Microservice course project. Builds a RESTful User/Address service across 6 lessons, ending with full CRUD, SQLite persistence via SQLAlchemy, and bearer token auth.

### Branch Structure

Each branch holds the **completed code from the previous lesson**:

| Branch | Contains final code from | State |
|---|---|---|
| `lesson-1` | (seed) | Docker scaffolding only |
| `lesson-2` | Lesson 1 | Health check endpoint |
| `lesson-2-1` | Lesson 2 | + GET /user/{id} |
| `lesson-3` | Lesson 2-1 | + POST /user/ (current most complete) |

Future lessons (3–6) will add: SQLAlchemy/SQLite persistence, a repository layer, Address CRUD, and bearer token auth.

## Running the App

```bash
# Docker (recommended)
docker compose up okcoders-python-fastapi

# Local
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

- API: `http://localhost:8000`
- Swagger docs: `http://localhost:8000/user/docs`

No automated tests or linters are configured.

## Architecture

Requests flow through three layers:

```
api/          → Route handlers (FastAPI APIRouter), input/output only
services/     → Business logic, static methods, returns JSONResponse
schemas/      → Pydantic models for request/response validation
enums/        → String-valued Python enums
```

A **repository layer** (SQLAlchemy) will be added in later lessons. Services currently use mock data.

## Key Conventions

### Routers (`api/`)
- One file per domain (e.g., `user_api.py`, `health_api.py`)
- Routers are registered in `main.py` with a prefix and tag:
  ```python
  app.include_router(user_router, prefix="/user", tags=["User"])
  ```
- Route handlers delegate immediately to a service static method — no business logic in the API layer

### Services (`services/`)
- All methods are `@staticmethod`; service classes are never instantiated
- Return `JSONResponse` directly using `jsonable_encoder`:
  ```python
  from fastapi.responses import JSONResponse
  from fastapi.encoders import jsonable_encoder

  class UserService:
      @staticmethod
      def get_user(user_id: int) -> JSONResponse:
          ...
          return JSONResponse(status_code=200, content=jsonable_encoder(data))
  ```

### Schemas (`schemas/`)
- Separate `requests/` and `responses/` subdirectories
- Always use `ConfigDict` with `json_schema_extra` for OpenAPI examples:
  ```python
  from pydantic import BaseModel, ConfigDict

  class UserResponseSchema(BaseModel):
      id: int
      name: str
      email: str | None

      model_config = ConfigDict(
          json_schema_extra={"example": {"id": 1, "name": "Jane", "email": "jane@example.com"}}
      )
  ```
- Use Python 3.10+ union syntax: `str | None` (not `Optional[str]`)

### Enums (`enums/`)
- Inherit from `enum.Enum` with string values:
  ```python
  import enum

  class HealthStatuses(enum.Enum):
      HEALTHY = "healthy"
      UNHEALTHY = "unhealthy"
  ```
- Used as type hints in schemas; Pydantic serializes to the string value

### `main.py`
- CORS middleware allows all origins (`allow_origins=["*"]`)
- Global exception handler catches unhandled exceptions and returns a JSON error response
- Add new routers here when introducing a new domain (e.g., Address in Lesson 4)
