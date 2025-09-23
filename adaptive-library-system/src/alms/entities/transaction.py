from abc import ABC, abstractmethod
from ..exceptions import (
    BookNotFoundError,
    UserNotFoundError,
    BookNotAvailableError,
    TransactionError,
)


class Transaction(ABC):
    def __init__(self, user_id, isbn):
        self.user_id = str(user_id)
        self.isbn = str(isbn)

    @abstractmethod
    def process(self, library):
        pass


class BorrowTransaction(Transaction):
    def process(self, library):
        user = library.get_user(self.user_id)
        if user is None:
            raise UserNotFoundError("User was not found.")
        book = library.get_book(self.isbn)
        if book is None:
            raise BookNotFoundError("Book was not found.")
        if not book.is_available():
            raise BookNotAvailableError("No copies available to borrow.")
        ok = book.borrow_one()
        if not ok:
            raise TransactionError("Could not borrow book.")
        user.borrow_isbn(self.isbn)
        return True


class ReturnTransaction(Transaction):
    def process(self, library):
        user = library.get_user(self.user_id)
        if user is None:
            raise UserNotFoundError("User was not found.")
        book = library.get_book(self.isbn)
        if book is None:
            raise BookNotFoundError("Book was not found.")
        ok_user = user.return_isbn(self.isbn)
        ok_book = book.return_one()
        if not (ok_user and ok_book):
            raise TransactionError("Could not return book.")
        return True