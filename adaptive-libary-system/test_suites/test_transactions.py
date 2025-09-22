import pytest
from alms.library import Library
from alms.entities.book import Book
from alms.entities.user import User
from alms.exceptions import BookNotAvailableError


@pytest.fixture()
def sample_library():
    lib = Library()
    lib.add_book(Book("111", "Clean Code", "Robert Martin", total_copies=1))
    lib.add_user(User("u1", "Alice", "alice@example.com"))
    return lib


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


def test_borrow_unavailable_raises(sample_library):
    lib = sample_library
    lib.borrow_book("u1", "111")
    with pytest.raises(BookNotAvailableError):
        lib.borrow_book("u1", "111")