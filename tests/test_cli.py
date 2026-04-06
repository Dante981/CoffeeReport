from unittest.mock import Mock
from argparse import Namespace
from src.coffee_report.cli import parse_args, Application

def test_parse_args():

    import sys
    from io import StringIO
    sys.argv = ['script.py', '--files', 'f1.csv', 'f2.csv', '--report', 'median-coffee']
    args = parse_args()
    assert args.files == ['f1.csv', 'f2.csv']
    assert args.report == 'median-coffee'

def test_application_orchestration():
    mock_loader = Mock(return_value={'test': [100.0]})
    mock_factory = Mock()
    mock_report = Mock(return_value={'test': 100.0})
    mock_factory.create.return_value = mock_report
    mock_presenter = Mock()
    
    app = Application(mock_loader, mock_factory, mock_presenter)
    app.run(['files'], 'median-coffee')
    
    mock_loader.load.assert_called_once_with(['files'])
    mock_factory.create.assert_called_once_with('median-coffee')
    mock_presenter.display.assert_called_once()