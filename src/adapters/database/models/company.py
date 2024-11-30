from sqlalchemy import Column, String, TIMESTAMP, UUID, ForeignKey
from ..connection import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    document = Column(String(14), unique=True, nullable=False)
    plan_id = Column(UUID(as_uuid=True), ForeignKey("plans.id"), nullable=False)
    created_at = Column(TIMESTAMP, default=None)
    updated_at = Column(TIMESTAMP, default=None)

    def __init__(self, name, email, document, plan_id):
        self.name = name
        self.email = email
        self.document = document
        self.plan_id = plan_id