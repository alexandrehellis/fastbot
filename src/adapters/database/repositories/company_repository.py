from ..models import Company
from .base_repository import BaseRepository

class CompanyRepository(BaseRepository):
    def get_all(self):
        return self.db.query(Company).all()
    
    def get_by_id(self, company_id):
        return self.db.query(Company).filter(Company.id == company_id).first()