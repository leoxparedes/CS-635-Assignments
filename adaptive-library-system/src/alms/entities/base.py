from typing import Dict

 # Simple base class that gives every entity an identifier and a to_dict helper
class BaseEntity:
    def __init__(self, identifier: str) -> None:
        self._identifier: str = str(identifier)

    def get_id(self) -> str:
        return self._identifier

    def to_dict(self) -> Dict[str, str]:
        return {"id": self._identifier}