from argparse import ArgumentParser, Namespace
from typing import List

def parse_args() -> Namespace:
    parser = ArgumentParser(description="Coffee consumption reports")
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--report", required=True)
    return parser.parse_args()

class Application:
    def __init__(self, data_loader, report_factory, presenter):
        self.data_loader = data_loader
        self.report_factory = report_factory
        self.presenter = presenter

    def run (self, files: list[str], report_name: str) -> None:
        try:
            data = self.data_loader.load(files)
            report = self.report_factory.create(report_name)
            results = report.generate(data)
            self.presenter.display(results)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            raise SystemExit(1)
        except KeyError as e:
            print(f"Unknown report: {report_name}")
            raise SystemExit(1)