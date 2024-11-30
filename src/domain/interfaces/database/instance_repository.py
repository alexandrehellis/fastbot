from abc import ABC, abstractmethod
from typing import List, Optional
from adapters.database.models.instance import Instance

class InstanceRepositoryInterface(ABC):
    @abstractmethod
    def get_all(self) -> List[Instance]:
        pass

    @abstractmethod
    def get_by_company(self, company_id: str) -> Optional[Instance]:
        pass