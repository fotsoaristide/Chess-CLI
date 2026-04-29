"""A simple JSON storage class for saving and loading data to a file."""

import json
from pathlib import Path


class JsonStorage:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def load(self):
        if not self.file_path.exists():
            return []

        with open(self.file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self, data):
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)