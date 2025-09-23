from .exceptions import BookNotFoundError, UserNotFoundError
from .entities.book import Book
from .entities.user import User


class Library:
    def __init__(self):
        self._books_by_isbn = {}
        self._users_by_id = {}

    # Basic entity management
    def add_book(self, book):
        self._books_by_isbn[book.get_isbn()] = book

    def add_user(self, user):
        self._users_by_id[user.get_user_id()] = user

    def get_book(self, isbn):
        return self._books_by_isbn.get(str(isbn))

    def get_user(self, user_id):
        return self._users_by_id.get(str(user_id))

    # Simple search over books and users
    def search_books(self, text):
        text = str(text)
        return [b for b in self._books_by_isbn.values() if b.matches(text)]

    def search_users(self, text):
        text = str(text)
        return [u for u in self._users_by_id.values() if u.matches(text)]

    # Borrow/return methods 
    def borrow_book(self, user_id, isbn):
        from .entities.transaction import BorrowTransaction

        t = BorrowTransaction(user_id, isbn)
        return t.process(self)

    def return_book(self, user_id, isbn):
        from .entities.transaction import ReturnTransaction

        t = ReturnTransaction(user_id, isbn)
        return t.process(self)

    # Persistence helpers
    def to_dict(self):
        return {
            "books": [b.to_dict() for b in self._books_by_isbn.values()],
            "users": [u.to_dict() for u in self._users_by_id.values()],
        }

    @staticmethod
    def from_dict(data):
        lib = Library()
        for b in data.get("books", []):
            book = Book.from_dict(b)
            lib.add_book(book)
        for u in data.get("users", []):
            user = User.from_dict(u)
            lib.add_user(user)
        return lib