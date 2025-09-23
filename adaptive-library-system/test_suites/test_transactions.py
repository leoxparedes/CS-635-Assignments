import pytest
from src.alms.library import Library
from src.alms.entities.book import Book
from src.alms.entities.user import User
from src.alms.exceptions import BookNotAvailableError, TransactionError, UserNotFoundError


@pytest.fixture()
# Test for creating library
def sample_library():
    lib = Library()
    lib.add_book(Book("111", "Clean Code", "Robert Martin", total_copies=1))
    lib.add_user(User("u1", "Alice", "alice@example.com"))
    return lib

# Test for borrowing and returning to library
def test_successful_borrow_and_return(sample_library):
    lib = sample_library
    ok_borrow = lib.borrow_book("u1", "111")
    assert ok_borrow is True
    assert lib.get_book("111").get_available_copies() == 0
    assert "111" in lib.get_user("u1").get_borrowed_isbns()

    ok_return = lib.return_book("u1", "111")
    assert ok_return is True
    assert lib.get_book("111").get_available_copies() == 1
    assert "111" not in lib.get_user("u1").get_borrowed_isbns()

# Test for trying to return book to library when not borrowed
def test_return_book_not_borrowed(sample_library):
    lib = sample_library
    with pytest.raises(TransactionError):
        lib.return_book("u1", "111")
    assert lib.get_book("111").get_available_copies() == lib.get_book("111").get_total_copies()


# Test for borrowing an unavailable book
def test_borrow_unavailable_raises(sample_library):
    lib = sample_library
    lib.borrow_book("u1", "111")
    with pytest.raises(BookNotAvailableError):
        lib.borrow_book("u1", "111")

# Test for borrowing a book when user doesn't exist
def test_borrow_with_invalid_user(sample_library):
    lib = sample_library
    with pytest.raises(UserNotFoundError):
        lib.borrow_book("invalid_user", "111")

# Test for borrowing and returning books multiple times
def test_borrow_then_return_multiple_times(sample_library):
    lib = sample_library
    lib.add_book(Book("222", "Advance OOP", "John Smith", total_copies=1))
    lib.get_book("111").total_copies = 2
    lib.get_book("222").total_copies = 2
    assert lib.borrow_book("u1", "111") is True
    lib.add_user(User("u2", "Bob", "bob@example.com"))
    assert lib.borrow_book("u2", "222") is True
    assert lib.return_book("u1", "111") is True
    assert lib.borrow_book("u1", "111") is True
    

