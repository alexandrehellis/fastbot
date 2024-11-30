from ..models import Instance
from .base_repository import BaseRepository

class InstanceRepository(BaseRepository):
    def get_all(self):
        return self.db.query(Instance).all()
    
    def get_by_company(self, company_id):
        return self.db.query(Instance).filter(Instance.company_id == company_id).all()