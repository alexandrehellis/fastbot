from abc import ABC, abstractmethod
from typing import List, Optional
from adapters.database.models.payment import Payment

class PaymentRepositoryInterface(ABC):
    @abstractmethod
    def get_all(self) -> List[Payment]:
        pass

    @abstractmethod
    def get_by_company(self, company_id: str) -> Optional[Payment]:
        pass