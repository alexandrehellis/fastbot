from abc import ABC, abstractmethod
from typing import List, Optional
from adapters.database.models.plan import Plan

class PlanRepositoryInterface(ABC):
    @abstractmethod
    def get_all(self) -> List[Plan]:
        pass

    @abstractmethod
    def get_by_id(self, plan_id: str) -> Optional[Plan]:
        pass