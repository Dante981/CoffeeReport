import pytest
from pathlib import Path
from src.coffee_report.data_loader import CSVDataLoader


@pytest.fixture
def sample_csv(tmp_path: Path):
    """CSV для всех тестов"""
    csv_file = tmp_path / "test.csv"
    lines = [
        "student,date,coffee_spent,sleep_hours",
        "Иван,2024-01-01,600,3.0",
        "Иван,2024-01-02,700,2.5",
        "Алексей,2024-01-01,450,4.5",
        "Алексей,2024-01-02,550,4.0"
    ]
    content = "\n".join(lines)
    csv_file.write_text(content, encoding="utf-8")
    return csv_file

@pytest.fixture
def sample_data():
    return {
        'Иван': [600.0, 700.0],
        'Алексей': [450.0, 550.0]
    }