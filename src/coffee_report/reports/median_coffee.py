from statistics import median
from typing import Dict, List
from .base import Report


class MedianCoffeeReport(Report):

    def generate(self, data: Dict[str, List[float]]) -> Dict[str, float]:
        results = {}
        for student, spends in data.items():
            if spends:
                results[student] = median(spends)
            else:
                results[student] = 0.0
            
        return dict(sorted(results.items(), key=lambda x: x[1], reverse=True))