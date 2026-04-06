from argparse import Namespace
import sys

from .cli import parse_args, Application
from .data_loader import CSVDataLoader
from .reports import ReportFactory
from .presenters import TabulatePresenter

def main() -> None:

    try:
        args = parse_args()

        data_loader = CSVDataLoader()
        report_factory = ReportFactory()
        presenter = TabulatePresenter()

        app = Application(data_loader, report_factory, presenter)
        app.run(args.files, args.report)

    except KeyboardInterrupt:
        print("\nCancelled by user", file=sys.stderr)
        sys.exit(130)  
    except SystemExit:
        raise  
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)



if __name__ == "__main__":
    main()