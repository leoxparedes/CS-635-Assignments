from src.alms.library import Library
from src.alms.entities.book import Book
from src.alms.entities.user import User
from src.alms.persistence.file_manager import FileManager

# Basic check for adding entries and loading them
def test_save_and_load_roundtrip(tmp_path):
    file_path = tmp_path / "test_alms_1.json"

    lib = Library()
    lib.add_book(Book("111", "Clean Code", "Robert Martin", total_copies=2))
    lib.add_user(User("u1", "Alice", "alice@example.com"))

    fm = FileManager(str(file_path))
    fm.save(lib)

    loaded = fm.load(Library)

    book = loaded.get_book("111")
    user = loaded.get_user("u1")

    assert book is not None
    assert user is not None
    assert book.get_title() == "Clean Code"
    assert user.get_name() == "Alice"


# Check for adding entries and searching for books and users not in library
def test_not_matching_book_and_user(tmp_path):
    file_path = tmp_path / "test_alms_2.json"

    lib = Library()
    lib.add_book(Book("111", "Clean Code", "Robert Martin", total_copies=2))
    lib.add_user(User("u1", "Alice", "alice@example.com"))

    fm = FileManager(str(file_path))
    fm.save(lib)

    loaded = fm.load(Library)

    # Test that these books and users don't exist in the file manager
    book = loaded.get_book("111")
    user = loaded.get_user("u1")

    assert book.get_title() != "Intro to Programming"
    assert user.get_name() != "Bob"

# Check for no files
def test_load_nonexistent_file(tmp_path):
    file_path = tmp_path / "test_alms_3.json"
    fm = FileManager(str(file_path))
    lib = fm.load(Library)
    assert isinstance(lib, Library)