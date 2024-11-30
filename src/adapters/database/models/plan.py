from sqlalchemy import Column, String, Float, Integer, TIMESTAMP, UUID
from ..connection import Base

class Plan(Base):
    __tablename__ = "plans"

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String, nullable=False)
    monthly_cost = Column(Float, nullable=False)
    anual_cost = Column(Float, nullable=False)
    user_limit = Column(Integer, nullable=False)
    instance_limit = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, default=None)
    updated_at = Column(TIMESTAMP, default=None)

    def __init__(self, name, description, monthly_cost, anual_cost, user_limit, instance_limit):
        self.name = name
        self.description = description
        self.monthly_cost = monthly_cost
        self.anual_cost = anual_cost
        self.user_limit = user_limit
        self.instance_limit = instance_limit