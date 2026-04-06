from typing import Dict, Any
from tabulate import tabulate

class TabulatePresenter:

    def display(self, data: Dict[str, Any]) -> None:
        if not data:
            print("No data to display")
            return
        table = [(student, f"{value:.1f}") for student, value in data.items()]

        print(tabulate(table, headers=["Student", "Median Cofee"],
                        tablefmt="grid", floatfmt=".1f"))