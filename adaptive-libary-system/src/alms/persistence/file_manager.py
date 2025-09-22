import json

class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, library):
        data = library.to_dict()
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load(self, library_class):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return library_class.from_dict(data)
        except FileNotFoundError:
            return library_class()