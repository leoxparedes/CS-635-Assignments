from typing import List, Optional, Type
from .exceptions import BookNotFoundError, UserNotFoundError
from .entities.book import Book
from .entities.user import User
from .entities.transaction import BorrowTransaction, ReturnTransaction, Transaction

# Library class that is used to add and search for books
class Library:
    def __init__(self) -> None:
        self._books_by_isbn: dict[str, Book] = {}
        self._users_by_id: dict[str, User] = {}

    # Basic entity management
    def add_book(self, book: Book) -> None:
        self._books_by_isbn[book.get_isbn()] = book

    def add_user(self, user: User) -> None:
        self._users_by_id[user.get_user_id()] = user

    def get_book(self, isbn: str) -> Optional[Book]:
        return self._books_by_isbn.get(str(isbn))

    def get_user(self, user_id: str) -> Optional[User]:
        return self._users_by_id.get(str(user_id))

    # Simple search over books and users
    def search_books(self, text: str) -> List[Book]:
        text = str(text)
        return [b for b in self._books_by_isbn.values() if b.matches(text)]

    def search_users(self, text: str) -> List[User]:
        text = str(text)
        return [u for u in self._users_by_id.values() if u.matches(text)]

    # Borrow/return methods 
    def borrow_book(self, user_id: str, isbn: str) -> bool:
        t: Transaction = BorrowTransaction(user_id, isbn)
        return t.process(self)

    def return_book(self, user_id: str, isbn: str) -> bool:
        t: Transaction = ReturnTransaction(user_id, isbn)
        return t.process(self)

    # Persistence helpers for saving and retrieving objects (books and users)
    def to_dict(self) -> dict[str, list[dict]]:
        return {
            "books": [b.to_dict() for b in self._books_by_isbn.values()],
            "users": [u.to_dict() for u in self._users_by_id.values()]
        }

    @staticmethod
    def from_dict(data: dict) -> "Library":
        lib = Library()
        for b in data.get("books", []):
            book = Book.from_dict(b)
            lib.add_book(book)
        for u in data.get("users", []):
            user = User.from_dict(u)
            lib.add_user(user)
        return lib