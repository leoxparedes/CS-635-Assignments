import pytest
from alms.entities.book import Book
from alms.entities.user import User

def test_book_basic_fields_and_availability():
    book = Book("123", "Title", "Author", total_copies=2)
    assert book.get_isbn() == "123"
    assert book.get_title() == "Title"
    assert book.get_author() == "Author"
    assert book.get_total_copies() == 2
    assert book.get_available_copies() == 2
    assert book.is_available() is True


def test_book_borrow_and_return_simple():
    book = Book("123", "T", "A", total_copies=1)
    assert book.borrow_one() is True
    assert book.is_available() is False
    assert book.return_one() is True
    assert book.is_available() is True


def test_user_basic_and_search():
    user = User("u1", "Alice Example", "alice@example.com")
    user.borrow_isbn("123")
    assert "123" in user.get_borrowed_isbns()
    assert user.matches("alice") is True
    assert user.return_isbn("123") is True