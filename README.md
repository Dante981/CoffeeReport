# Coffee Report 🥤📈

**CLI-утилита для анализа расходов студентов на кофе во время сессии.**  

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)

## Быстрый старт

```powershell
# Windows
.venv\Scripts\Activate.ps1
pip install -e .
coffee-report --files examples/data/*.csv --report median-coffee

# Linux/Mac
pip install -e .
coffee-report --files data/*.csv --report median-coffee
```

## Архитектура проекта

```text
coffeereport/                    # Корень репозитория
├── README.md                    # Документация
├── pyproject.toml               # Зависимости + entrypoint
├── .gitignore                   
├── LICENSE                      # MIT
│
├── src/                         # Основной пакет (PEP 582)
│   └── coffee_report/
│       ├── __init__.py          # __version__ = "0.1.0"
│       ├── main.py              # CLI entrypoint
│       ├── cli.py               # parse_args() + Application
│       ├── data_loader.py       # CSV → dict[student, spends]
│       ├── presenters.py        # tabulate таблицы
│       └── reports/             # Plugin система!
│           ├── __init__.py      # ReportFactory
│           ├── base.py          # ABC Report interface
│           └── median_coffee.py # Конкретная реализация
│
├── tests/                       # pytest
│   ├── conftest.py              # fixtures (sample_csv)
│   ├── test_cli.py
│   ├── test_data_loader.py
│   ├── test_presenters.py
│   └── test_reports/
│
└── examples/                    # примеры
    ├── data/
    │   └── test.csv
    ├── screenshot-cli.png
    └── screenshot-tests.png
```

## Пример вывода
```bash
$ coffee-report --files examples/data/*.csv --report median-coffee
```
```text
+---------------+--------------+
| Student       | Median Coffee|
+===============+==============+
| Иван Кузнецов | 650.0        |
| Алексей Смирнов| 500.0       |
| Павел Новиков | 420.0        |
| Елена Волкова | 310.0        |
| Дарья Петрова | 250.0        |
| Мария Соколова| 120.0        |
+---------------+==============+
```


## Тестирование.

### Установка тестовых зависимостей
```bash
pip install -e .[test]
```

### Все тесты + покрытие
```bash
python -m pytest --cov
```
### Только быстрые тесты
```bash
python -m pytest tests/ -v
```
