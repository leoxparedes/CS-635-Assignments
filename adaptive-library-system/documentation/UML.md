# UML Diagram 
```mermaid
classDiagram
direction LR

namespace alms {
  class Library {
    - _books_by_isbn: dict
    - _users_by_id: dict
    + add_book(b: Book)
    + add_user(u: User)
    + get_book(isbn: str): Book?
    + get_user(uid: str): User?
    + search_books(q: str): Book[]
    + search_users(q: str): User[]
    + borrow_book(uid: str, isbn: str): bool
    + return_book(uid: str, isbn: str): bool
    + to_dict(): dict
    + from_dict(data: dict) Library
  }

  class Searchable {
    <<interface>>
    + matches(text: str): bool
  }

  class Transaction {
    <<abstract>>
    + user_id: str
    + isbn: str
    + process(lib: Library) bool
  }

  class BorrowTransaction {
    + process(lib: Library) bool
  }

  class ReturnTransaction {
    + process(lib: Library) bool
  }

  class BookNotFoundError
  class UserNotFoundError
  class BookNotAvailableError
  class TransactionError
}

namespace alms.entities {
  class BaseEntity {
    - _identifier: str
    + get_id(): str
    + to_dict(): dict
  }

  class Book {
    - _isbn: str
    - _title: str
    - _author: str
    - _total_copies: int
    - _available_copies: int
    + is_available(): bool
    + borrow_one(): bool
    + return_one(): bool
    + matches(text: str): bool
    + to_dict(): dict
    + from_dict(data: dict) Book
  }

  class User {
    - _user_id: str
    - _name: str
    - _email: str
    - _borrowed_isbns: str[]
    + borrow_isbn(isbn: str)
    + return_isbn(isbn: str) bool
    + matches(text: str): bool
    + to_dict(): dict
    + from_dict(data: dict) User
  }
}

namespace alms.persistence {
  class FileManager {
    + file_path: str
    + save(lib: Library)
    + load(library_class) Library
  }
}
alms.entities.Book --|> alms.entities.BaseEntity
alms.entities.User --|> alms.entities.BaseEntity
alms.entities.Book ..|> alms.Searchable
alms.entities.User ..|> alms.Searchable
alms.BorrowTransaction --|> alms.Transaction
alms.ReturnTransaction --|> alms.Transaction

alms.Library "1" o-- "*" alms.entities.Book : manages
alms.Library "1" o-- "*" alms.entities.User : manages
alms.Transaction ..> alms.Library : process()
alms.persistence.FileManager ..> alms.Library : save/load