from abc import ABC, abstractmethod

class EvolutionApiInterface(ABC):
    @abstractmethod
    def send_message(self, data: dict) -> dict:
        pass