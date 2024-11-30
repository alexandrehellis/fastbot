from ..models import User
from .base_repository import BaseRepository

class UserRepository(BaseRepository):
    def get_all(self):
        return self.db.query(User).all()
    
    def get_by_email(self, email):
        return self.db.query(User).filter(User.email == email).first()