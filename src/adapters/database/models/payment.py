from sqlalchemy import Column, Float, Boolean, TIMESTAMP, UUID, ForeignKey
from ..connection import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(UUID(as_uuid=True), primary_key=True)
    company_id = Column(UUID(as_uuid=True), ForeignKey("companies.id"), nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(TIMESTAMP, default=None)
    status = Column(Boolean, default=False, nullable=False)

    def __init__(self, company_id, amount, payment_date=None, status=False):
        self.company_id = company_id
        self.amount = amount
        self.payment_date = payment_date
        self.status = status