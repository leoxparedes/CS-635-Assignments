from abc import ABC, abstractmethod
#Using abstract base class (ABC) library for these abstract classes

#Searchable for verify user or book matches
class Searchable(ABC):
    @abstractmethod
    def matches(self, query):
        pass
#Transaction methods for processing transactions
class Transaction(ABC):
    @abstractmethod
    def process(self, library: "Library"):
        pass
    #May need to change if class to_dict changes
    @abstractmethod
    def to_dict(self):
        pass
