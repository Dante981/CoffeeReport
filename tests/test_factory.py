import pytest
from src.coffee_report.reports import ReportFactory

def test_factory_create():
    report = ReportFactory.create('median-coffee')
    assert hasattr(report, 'generate')

def test_unknown_report():
    with pytest.raises(KeyError, match="Unknown report"):
        ReportFactory.create('wrong')