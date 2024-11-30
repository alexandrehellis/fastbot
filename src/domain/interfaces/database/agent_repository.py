from abc import ABC, abstractmethod
from typing import List, Optional
from adapters.database.models.agent import Agent

class AgentRepositoryInterface(ABC):
    @abstractmethod
    def get_all(self) -> List[Agent]:
        pass

    @abstractmethod
    def get_by_company(self, company_id: str) -> Optional[Agent]:
        pass
