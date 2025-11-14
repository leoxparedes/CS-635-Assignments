import json
from typing import Type, TypeVar
from ..library import Library

T = TypeVar("T", bound=Library)

class FileManager:
    def __init__(self, file_path: str) -> None:
        self.file_path: str = file_path

    def save(self, library: Library) -> None:
        data = library.to_dict()
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load(self, library_class: Type[T]) -> T:
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return library_class.from_dict(data)
        except FileNotFoundError:
            return library_class()