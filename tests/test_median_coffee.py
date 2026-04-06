from src.coffee_report.reports.median_coffee import MedianCoffeeReport

def test_median_calculation(sample_data):
    report = MedianCoffeeReport()
    result = report.generate(sample_data)
    assert result == {
        'Иван': 650.0,      
        'Алексей': 500.0  
    }

def test_sorted_by_median():
    data = {'A': [100], 'B': [1000]}
    result = MedianCoffeeReport().generate(data)
    assert list(result.keys())[0] == 'B' 

def test_empty_list():
    result = MedianCoffeeReport().generate({'empty': []})
    assert result['empty'] == 0.0