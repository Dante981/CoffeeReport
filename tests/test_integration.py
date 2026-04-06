import subprocess
import pytest
import sys

def test_cli_end_to_end(tmp_path, sample_csv):



    result = subprocess.run([
        sys.executable, '-m', 'src.coffee_report.main',
        '--files', str(sample_csv),
        '--report', 'median-coffee'
    ], capture_output=True, text=True)
    
    assert result.returncode == 0
    
    assert "Иван" in result.stdout
    assert "650.0" in result.stdout