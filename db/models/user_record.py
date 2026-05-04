from sqlalchemy import Boolean, Column, String

from db.connection import Base

class UserRecord(Base):
    __tablename__ = "user"
    id = Column(String, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
