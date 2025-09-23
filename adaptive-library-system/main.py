from src.alms.library import Library
from src.alms.entities.book import Book
from src.alms.entities.user import User
from src.alms.persistence.file_manager import FileManager


def build_sample_library():
    library = Library()
    library.add_book(Book("111", "Clean Code", "Robert Martin", total_copies=2))
    library.add_book(Book("222", "The Pragmatic Programmer", "Andrew Hunt", total_copies=1))
    library.add_user(User("u1", "Alice", "alice@example.com"))
    library.add_user(User("u2", "Bob", "bob@example.com"))
    return library


def demo():
    file_manager = FileManager("alms_data.json")
    library = file_manager.load(Library)

    if not library.search_books("") and not library.search_users(""):
        library = build_sample_library()
        file_manager.save(library)

    print("=== Books ===")
    for b in library.search_books(""):
        print(b.get_isbn(), b.get_title(), b.get_author(), b.get_available_copies())

    print("\nBorrow '111' for user 'u1'")
    library.borrow_book("u1", "111")
    file_manager.save(library)

    print("Available copies for 111:", library.get_book("111").get_available_copies())

    print("\nReturn '111' for user 'u1'")
    library.return_book("u1", "111")
    file_manager.save(library)

    print("Available copies for 111:", library.get_book("111").get_available_copies())


if __name__ == "__main__":
    demo()