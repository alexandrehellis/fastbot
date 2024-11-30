from abc import ABC, abstractmethod
from typing import List, Optional
from adapters.database.models.company import Company

class CompanyRepositoryInterface(ABC):
    @abstractmethod
    def get_all(self) -> List[Company]:
        pass

    @abstractmethod
    def get_by_id(self, company_id: str) -> Optional[Company]:
        pass