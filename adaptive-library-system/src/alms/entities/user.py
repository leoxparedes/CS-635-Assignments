from typing import Dict, List
from .base import BaseEntity
from ..interfaces import Searchable

class User(BaseEntity, Searchable):
    def __init__(self, user_id: str, name: str, email: str) -> None:
        super().__init__(user_id)
        self._user_id: str = str(user_id)
        self._name: str = name
        self._email: str = email
        self._borrowed_isbns: List[str] = []

    # Encapsulated getters
    def get_user_id(self) -> str:
        return self._user_id

    def get_name(self) -> str:
        return self._name

    def get_email(self) -> str:
        return self._email

    def get_borrowed_isbns(self) -> List[str]:
        return list(self._borrowed_isbns)

    # Borrow / return and checking availabiltiy logic
    def borrow_isbn(self, isbn: str) -> None:
        self._borrowed_isbns.append(str(isbn))

    def return_isbn(self, isbn: str) -> bool:
        isbn = str(isbn)
        if isbn in self._borrowed_isbns:
            self._borrowed_isbns.remove(isbn)
            return True
        return False

    # Search interface
    def matches(self, text: str) -> bool:
        text = str(text).lower()
        return (
            text in self._user_id.lower() or
            text in self._name.lower() or
            text in self._email.lower()
        )

    # Method for setting a new user object in dictionary (Serialization)
    def to_dict(self) -> Dict[str, object]:
        return {
            "user_id": self._user_id,
            "name": self._name,
            "email": self._email,
            "borrowed_isbns": list(self._borrowed_isbns),
        }

    # Static method for getting user and their borrowed copies from dictionary
    @staticmethod
    def from_dict(data: Dict[str, object]) -> "User":
        user = User(
            data.get("user_id", ""),
            data.get("name", ""),
            data.get("email", "")
        )
        user._borrowed_isbns = list(data.get("borrowed_isbns", []))
        return user