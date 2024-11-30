from sqlalchemy import Column, String, Boolean, TIMESTAMP, UUID, ForeignKey
from ..connection import Base

class Instance(Base):
    __tablename__ = "instances"

    id = Column(UUID(as_uuid=True), primary_key=True)
    company_id = Column(UUID(as_uuid=True), ForeignKey("companies.id"), nullable=False)
    name = Column(String(255), nullable=False)
    token = Column(String(255), nullable=False)
    status = Column(Boolean, default=False, nullable=False)
    created_at = Column(TIMESTAMP, default=None)
    updated_at = Column(TIMESTAMP, default=None)

    def __init__(self, company_id, name, token, status=False):
        self.company_id = company_id
        self.name = name
        self.token = token
        self.status = status