# strategy/waste_disposal_strategy.py
from abc import ABC, abstractmethod

class WasteDisposalStrategy(ABC):
    @abstractmethod
    def dispose_waste(self, waste_data):
        pass
