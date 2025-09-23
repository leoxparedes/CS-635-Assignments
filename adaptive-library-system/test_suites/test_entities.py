import pytest
from src.alms.entities.book import Book
from src.alms.entities.user import User

## BOOK TESTS ##
# Test for book and availability
def test_book_basic_fields_and_availability():
    book = Book("123", "Title", "Author", total_copies=2)
    assert book.get_isbn() == "123"
    assert book.get_title() == "Title"
    assert book.get_author() == "Author"
    assert book.get_total_copies() == 2
    assert book.get_available_copies() == 2
    assert book.is_available() is True

# Test for book and no availability
def test_book_basic_fields_and_no_availability():
    book = Book("123", "Title", "Author", total_copies=2)
    assert book.get_isbn() == "123"
    assert book.get_title() == "Title"
    assert book.get_author() == "Author"
    assert book.get_total_copies() == 2
    assert book.borrow_one() is True
    assert book.borrow_one() is True
    assert book.get_available_copies() == 0
    assert book.is_available() is False

# Test for borrowing book and returning book
def test_book_borrow_and_return_simple():
    book = Book("123", "T", "A", total_copies=1)
    assert book.borrow_one() is True
    assert book.is_available() is False
    assert book.return_one() is True
    assert book.is_available() is True

# Test for borrwoing book and checking in after failing to find available one
def test_book_borrow_and_return_advanced():
    book = Book("900", "Linux 101", "Linus Torvalds", total_copies=2)
    assert book.borrow_one() is True
    assert book.is_available() is True
    assert book.borrow_one() is True
    assert book.is_available() is False
    assert book.return_one() is True
    assert book.is_available() is True

# Test for returning with no checked out books
def test_return_when_none_borrowed():
    book = Book("888", "Return Nothing", "Author", total_copies=1)
    assert book.return_one() is False
    assert book.get_available_copies() == 1

## USER TESTS ##
# Test for creating user and searching user
def test_user_basic_and_search():
    user = User("u1", "Alice Carter", "alice@example.com")
    user.borrow_isbn("123")
    assert "123" in user.get_borrowed_isbns()
    assert user.matches("alice") is True
    assert user.return_isbn("123") is True

# Test for creating user and not finding user when searching
def test_user_basic_and_search_not_found():
    user = User("u1", "Bob Smith", "bob@example.com")
    user.borrow_isbn("123")
    assert "123" in user.get_borrowed_isbns()
    assert user.matches("alice") is False
    assert user.return_isbn("123") is True

# Test for user borrowing multiple books
def test_user_borrow_multiple_books():
    user = User("u2", "Charlie", "charlie@example.com")
    user.borrow_isbn("111")
    user.borrow_isbn("222")
    borrowed = user.get_borrowed_isbns()
    assert "111" in borrowed
    assert "222" in borrowed

# Test for searching for a user with partial name
def test_user_search_partial_match():
    user = User("u4", "Edward Johnson", "edward@example.com")
    assert user.matches("Edw") is True
    assert user.matches("john") is True
    assert user.matches("notfound") is False