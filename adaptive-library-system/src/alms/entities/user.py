from .base import BaseEntity
from ..interfaces import Searchable


class User(BaseEntity, Searchable):
    def __init__(self, user_id, name, email):
        super().__init__(user_id)
        self._user_id = str(user_id)
        self._name = name
        self._email = email
        self._borrowed_isbns = []

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_borrowed_isbns(self):
        return list(self._borrowed_isbns)

    def borrow_isbn(self, isbn):
        self._borrowed_isbns.append(str(isbn))

    def return_isbn(self, isbn):
        isbn = str(isbn)
        if isbn in self._borrowed_isbns:
            self._borrowed_isbns.remove(isbn)
            return True
        return False

    def matches(self, text):
        text = str(text).lower()
        return (
            text in self._user_id.lower()
            or text in self._name.lower()
            or text in self._email.lower()
        )

    def to_dict(self):
        return {
            "user_id": self._user_id,
            "name": self._name,
            "email": self._email,
            "borrowed_isbns": list(self._borrowed_isbns),
        }

    @staticmethod
    def from_dict(data):
        user = User(data.get("user_id"), data.get("name"), data.get("email"))
        user._borrowed_isbns = list(data.get("borrowed_isbns", []))
        return user