from typing import Dict, Any
from ..interfaces import Searchable
from ..exceptions import BookUnavailableError

#Book class that defines properties of books and tracks stock
class Book(Searchable):
    def __init__(self, book_name, author, isbn, stock, full_stock):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__stock = stock
        self.__full_stock = full_stock
        self.__return_date = return_date
    #Get book title
    def title(self):
        return self._title
    #Get book author
    def author(self):
        return self.__author
    #Get book isbn
    def isbn(self):
        return self.__isbn
    #Get current stock
    def stock(self):
        return self.__stock
    #Get full amount of books when all checked in 
    def full_stock(self):
        return self.__full_stock
    #Get dude date to return book
    def return_date(self):
        return self.__return_date
    #Check out book and raise error if out of stock
    def check_out(self):
        if self.__stock <= 0:
            raise BookUnavailableError(f"Book '{self.__title}' is out of stock")
        self.__stock -= 1
    #Check in book
    def check_in(self):
        if self.__stock < self.__full_stock:
            self.__stock += 1
    #Verify book matches search book
    def matches(self, query: str) -> bool:
        q = query.lower()
        return q in self.__title.lower() or q in self.__author.lower() or q in self.__isbn.lower()

    #To dictionary of objects storing ALMS Objects
    def to_dict(self):
        return dict(
            title = self.__title,
            author = self.__author,
            isbn = self.__isbn,
            full_stock = self.__full_stock,
            stock = self.__stock,
        )

    #From dictionary of objects retrieving ALMS Objects
    def from_dict(data: Dict[str, Any]):
        book = Book(data["title"], data["author"], data["isbn"], data.get("total_copies", 1), data.get("id"))
        book.__stock = data.get("available_stock", book.__stock)
        return book
