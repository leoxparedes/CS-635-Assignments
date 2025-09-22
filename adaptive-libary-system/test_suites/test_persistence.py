from alms.library import Library
from alms.entities.book import Book
from alms.entities.user import User
from alms.persistence.file_manager import FileManager


def test_save_and_load_roundtrip(tmp_path):
    file_path = tmp_path / "alms.json"

    lib = Library()
    lib.add_book(Book("111", "Clean Code", "Robert Martin", total_copies=2))
    lib.add_user(User("u1", "Alice", "alice@example.com"))

    fm = FileManager(str(file_path))
    fm.save(lib)

    loaded = fm.load(Library)

    # basic checks
    book = loaded.get_book("111")
    user = loaded.get_user("u1")

    assert book is not None
    assert user is not None
    assert book.get_title() == "Clean Code"
    assert user.get_name() == "Alice"