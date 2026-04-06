from typing import Type, Dict
from .base import Report

from .median_coffee import MedianCoffeeReport


class ReportFactory:
    REPORTS: Dict[str, Type[Report]] = {
        'median-coffee': MedianCoffeeReport
    }

    @classmethod
    def create(cls, name: str) -> Report:

        report_class = cls.REPORTS.get(name)
        if report_class is None:
            raise KeyError(f"Unknown report type: '{name}'. "
                          f"Available: {list(cls.REPORTS)}")
        return report_class()

    @classmethod
    def list_reports(cls) -> list[str]:
        return list[cls.REPORTS.keys()]




__all__ = ['Report', 'ReportFactory', 'MedianCoffeeReport']