import pytest
from src.coffee_report.data_loader import CSVDataLoader


def test_load_single_file(sample_csv):
    loader = CSVDataLoader()
    data = loader.load([str(sample_csv)])
    expected = {
        'Иван': [600.0, 700.0],
        'Алексей': [450.0, 550.0]
    }
    assert data == expected

def test_multiple_files(tmp_path):
    f1 = tmp_path / "f1.csv"
    f2 = tmp_path / "f2.csv"
    f1.write_text("student,coffee_spent\nИван,100", encoding="utf-8")
    f2.write_text("student,coffee_spent\nИван,200", encoding="utf-8")
    
    
    loader = CSVDataLoader()
    data = loader.load([str(f1), str(f2)])
    assert sum(data['Иван']) == 300.0
    assert len(data['Иван']) == 2

def test_file_not_found():
    loader = CSVDataLoader()
    with pytest.raises(FileNotFoundError):
        loader.load(["nonexistent.csv"])