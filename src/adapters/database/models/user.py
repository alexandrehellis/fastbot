from sqlalchemy import Column, String, TIMESTAMP, UUID, ForeignKey
from ..connection import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True)
    company_id = Column(UUID(as_uuid=True), ForeignKey("companies.id"), nullable=False)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, default=None)
    updated_at = Column(TIMESTAMP, default=None)

    def __init__(self, company_id, name, email, password_hash, role):
        self.company_id = company_id
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.role = role