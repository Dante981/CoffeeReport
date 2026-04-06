from io import StringIO
import sys
from src.coffee_report.presenters import TabulatePresenter

def test_display_table(capfd):
    presenter = TabulatePresenter()
    data = {'Иван': 650.0, 'Алексей': 500.0}
    presenter.display(data)
    
    output = capfd.readouterr().out
    assert 'Иван' in output
    assert '650.0' in output
    assert '+' in output  # tabulate border

def test_empty_data(capfd):
    presenter = TabulatePresenter()
    presenter.display({})
    assert "No data" in capfd.readouterr().out