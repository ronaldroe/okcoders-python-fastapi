from uuid import uuid4

from schemas.base.base_user_schema import BaseUserSchema

from db.connection import SessionLocal
from db.models.user_record import UserRecord
from schemas.responses.user_response_schema import UserResponseSchema


class UserRepository:
    @staticmethod
    def get_user_by_id(user_id) -> UserResponseSchema:
        with SessionLocal() as db:
            user_record: UserRecord = (
                db.query(UserRecord)
                .filter(UserRecord.id == user_id)
                .one()
            )

        return UserResponseSchema(
            id=user_record.id,
            first_name=user_record.first_name,
            last_name=user_record.last_name,
            email=user_record.email,
            phone=user_record.phone,
            is_active=user_record.is_active
        )

    @staticmethod
    def create_user(user_schema: BaseUserSchema) -> UserResponseSchema:
        try:
            new_user = UserRecord(
                id=str(uuid4()),
                first_name=user_schema.first_name,
                last_name=user_schema.last_name,
                email=user_schema.email,
                phone=user_schema.phone,
                is_active=user_schema.is_active
            )

            with SessionLocal.begin() as db:
                db.add(new_user)

                response = UserResponseSchema(
                    id=new_user.id,
                    first_name=new_user.first_name,
                    last_name=new_user.last_name,
                    email=new_user.email,
                    phone=new_user.phone,
                    is_active=new_user.is_active
                )
            
            return response
        except Exception as e:
            raise e
