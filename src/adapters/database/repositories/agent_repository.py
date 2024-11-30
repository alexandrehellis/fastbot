from ..models import Agent
from .base_repository import BaseRepository

class AgentRepository(BaseRepository):
    def get_all(self):
        return self.db.query(Agent).all()
    
    def get_by_company(self, company_id):
        return self.db.query(Agent).filter(Agent.company_id == company_id).all()