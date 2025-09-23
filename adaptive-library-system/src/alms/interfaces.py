from abc import ABC, abstractmethod


class Searchable(ABC):
    @abstractmethod
    def matches(self, text):
        """Return True if this object matches the search text."""
        pass