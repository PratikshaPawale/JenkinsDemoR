import json
from pathlib import Path
from typing import Any


def load_json(filename: str) -> Any:
    path = Path(__file__).parent.parent / "testdata" / filename
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
