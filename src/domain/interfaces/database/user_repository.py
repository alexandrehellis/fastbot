from abc import ABC, abstractmethod
from typing import List, Optional
from adapters.database.models.user import User

class UserRepositoryInterface(ABC):
    @abstractmethod
    def get_all(self) -> List[User]:
        pass

    @abstractmethod
    def get_by_emal(self, email: str) -> Optional[User]:
        pass