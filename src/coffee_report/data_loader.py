from csv import DictReader
from pathlib import Path
from typing import Dict, List
from collections import defaultdict

class CSVDataLoader:
    REQUIRED_FIELDS = {"student", "coffee_spent"}

    def load(self, file_paths: List[str]) -> Dict[str, List[float]]:
        data = defaultdict(list)

        for path_str in file_paths:
            path = Path(path_str)
            if not path.exists():
                raise FileNotFoundError(f"File not found: {path}")


            with path.open("r", encoding="utf-8") as f:
                reader = DictReader(f)
                for row in reader:
                    try:
                        student = row["student"].strip()
                        coffee = float(row["coffee_spent"])
                        data[student].append(coffee)
                    except (ValueError, KeyError) as e:
                        print(f"Skipping invalid row in {path}: {e}")
                        continue

        return dict(data)
