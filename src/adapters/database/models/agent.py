from sqlalchemy import Column, String, Boolean, TIMESTAMP, UUID, ForeignKey
from ..connection import Base

class Agent(Base):
    __tablename__ = "agents"

    id = Column(UUID(as_uuid=True), primary_key=True)
    company_id = Column(UUID(as_uuid=True), ForeignKey("companies.id"), nullable=False)
    name = Column(String(255), nullable=False)
    objective = Column(String(255), nullable=False)
    description = Column(String, nullable=False)
    model = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(TIMESTAMP, default=None)
    updated_at = Column(TIMESTAMP, default=None)

    def __init__(self, company_id, name, objective, description, model, is_active=True):
        self.company_id = company_id
        self.name = name
        self.objective = objective
        self.description = description
        self.model = model
        self.is_active = is_active