from abc import ABC, abstractmethod

# Interface for searching that's used for users and books
class Searchable(ABC):
    @abstractmethod
    def matches(self, text: str) -> bool:
        # Return True if this object matches the search text
        pass