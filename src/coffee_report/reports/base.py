from abc import ABC, abstractmethod
from typing import Dict, List, Any

class Report(ABC):

    @abstractmethod
    def generate(self, data: Dict[str, List[float]]) -> Dict[str, Any]:
        pass