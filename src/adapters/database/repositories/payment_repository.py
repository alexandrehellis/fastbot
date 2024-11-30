from ..models import Payment
from .base_repository import BaseRepository

class PaymentRepository(BaseRepository):
    def get_all(self):
        return self.db.query(Payment).all()
    
    def get_by_company(self, company_id):
        return self.db.query(Payment).filter(Payment.company_id == company_id).all()