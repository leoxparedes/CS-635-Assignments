from .base import BaseEntity
from ..interfaces import Searchable


class Book(BaseEntity, Searchable):
    def __init__(self, isbn, title, author, total_copies=1):
        super().__init__(isbn)
        self._isbn = str(isbn)
        self._title = title
        self._author = author
        self._total_copies = int(total_copies)
        self._available_copies = int(total_copies)

    # Encapsulated getters
    def get_isbn(self):
        return self._isbn

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_total_copies(self):
        return self._total_copies

    def get_available_copies(self):
        return self._available_copies

    # Borrow / return and checking availabiltiy logic
    def is_available(self):
        return self._available_copies > 0

    def borrow_one(self):
        if self._available_copies > 0:
            self._available_copies -= 1
            return True
        return False

    def return_one(self):
        if self._available_copies < self._total_copies:
            self._available_copies += 1
            return True
        return False

    # Search interface
    def matches(self, text):
        text = str(text).lower()
        return (
            text in self._isbn.lower()
            or text in self._title.lower()
            or text in self._author.lower()
        )

    # Method for setting a new book object in dictionary
    def to_dict(self):
        return {
            "isbn": self._isbn,
            "title": self._title,
            "author": self._author,
            "total_copies": self._total_copies,
            "available_copies": self._available_copies,
        }

    # Static method for getting book and available copies from dictionary
    @staticmethod
    def from_dict(data):
        book = Book(
            data.get("isbn"),
            data.get("title"),
            data.get("author"),
            data.get("total_copies", 1),
        )
        # sync available copies
        book._available_copies = int(data.get("available_copies", book._total_copies))
        return book