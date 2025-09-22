from typing import Dict, Any
from ..interfaces import Searchable
from ..exceptions import TransactionError

#User that checks in/out books
class User(Searchable):
    def __init__(self, name, email, redId, checkedOut, limit):
        self.__name = name
        self.__email = email
        self.__redId = redId
        self.__checkedOut = checkedOut
        self.__limit = limit
    #Get user name
    def name(self):
        return self._name
    #Get email
    def email(self):
        return self._email
    #Get current amount of books checked out 
    def checkedOut(self):
        return self._checkedOut
    #Get limit of books able to be checked out 
    def limit(self):
        return self._limit
    #Check amount of checkout out books to see if user is allowed to borrow more
    def can_borrow(self):
         return len(self._checkedOut) < self._limit
    #Check out book
    def check_out_book(self, isbn: str, due_date: str):
        if not self.can_borrow():
            raise TransactionError(f"{self.__name} reached borrow limit.")
        self.__checkedOut[isbn] = due_date
    #Check in book
    def check_in_book(self, isbn: str):
        if isbn not in self.__checkedOut:
            raise TransactionError(f"{self.__name} didn’t borrow {isbn}")
        del self.__checkedOut[isbn]
    #Check if search matches
    def matches(self, query: str) -> bool:
        q = query.lower()
        return q in self.__name.lower() or q in self.__email.lower()
    #Send object to dictionary
    def to_dict(self):
        return dict(
            name=self.__name,
            email=self.__email,
            checkedOut=self.__checkedOut,
            limit =self.__limit,
        )
    #Retrieve object to dictionary
    def from_dict(data: Dict[str, Any]):
        user = User(data["name"], data["email"], data.get("redId"))
        user.__checkedOut = data.get("checkout_books", {})
        user.__limt = data.get("checkout_out_limit", 5)
        return user