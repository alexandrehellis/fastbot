from ..models import Plan
from .base_repository import BaseRepository

class PlanRepository(BaseRepository):
    def get_all(self):
        return self.db.query(Plan).all()
    
    def get_by_id(self, plan_id):
        return self.db.query(Plan).filter(Plan.id == plan_id).first()