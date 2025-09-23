# CS 635 Project 1: Adaptive Library Management System (ALMS)

## Contributors: Leo Paredes, Brandon Reynolds

# Getting started...
At the root directory enter the following in the terminal window.
1) python -m .venv
2) .venv\Scripts\activate
3) pip install pytest


# How to run pytest...
All tests for ALMS can be found in "test_suites/". To run tests, enter "pytest" in the terminal window. Pytest session will start, collect all tests, run all tests, and report PASS/FAIL. 

# Demo
A demo of the ALMS can be found in "main.py". To execute the demo, enter "python main.py" in the terminal window. 

# UML Diagram 
## UML Diagram

```mermaid
%% ALMS — UML (Mermaid class diagram)
classDiagram
direction LR

%% Packages (namespaces)
namespace alms {
  class Library {
    - _books_by_isbn: dict[str, Book]
    - _users_by_id: dict[str, User]
    + add_book(book: Book): void
    + add_user(user: User): void
    + get_book(isbn: str): Book|None
    + get_user(user_id: str): User|None
    + search_books(text: str): list[Book]
    + search_users(text: str): list[User]
    + borrow_book(user_id: str, isbn: str): bool
    + return_book(user_id: str, isbn: str): bool
    + to_dict(): dict
    + from_dict(data: dict) static: Library
  }

  class Searchable {
    <<interface>>
    + matches(text: str): bool
  }

  class Transaction {
    <<abstract>>
    + user_id: str
    + isbn: str
    + process(library: Library) *abstract*: bool
  }

  class BorrowTransaction {
    + process(library: Library): bool
  }

  class ReturnTransaction {
    + process(library: Library): bool
  }

  %% Exceptions
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
    + get_isbn(): str
    + get_title(): str
    + get_author(): str
    + get_total_copies(): int
    + get_available_copies(): int
    + is_available(): bool
    + borrow_one(): bool
    + return_one(): bool
    + matches(text: str): bool
    + to_dict(): dict
    + from_dict(data: dict) static: Book
  }

  class User {
    - _user_id: str
    - _name: str
    - _email: str
    - _borrowed_isbns: list[str]
    + get_user_id(): str
    + get_name(): str
    + get_email(): str
    + get_borrowed_isbns(): list[str]
    + borrow_isbn(isbn: str): void
    + return_isbn(isbn: str): bool
    + matches(text: str): bool
    + to_dict(): dict
    + from_dict(data: dict) static: User
  }
}

namespace alms.persistence {
  class FileManager {
    + file_path: str
    + save(library: Library): void
    + load(library_class: type[Library]): Library
  }
}

%% Inheritance / Implementation
alms.entities.Book --|> alms.entities.BaseEntity
alms.entities.User --|> alms.entities.BaseEntity
alms.entities.Book ..|> alms.Searchable
alms.entities.User ..|> alms.Searchable
alms.BorrowTransaction --|> alms.Transaction
alms.ReturnTransaction --|> alms.Transaction

%% Exceptions extend built-in Exception (omitted base for brevity)
alms.BookNotFoundError --|> Exception
alms.UserNotFoundError --|> Exception
alms.BookNotAvailableError --|> Exception
alms.TransactionError --|> Exception

%% Associations
alms.Library "1" o-- "*" alms.entities.Book : manages
alms.Library "1" o-- "*" alms.entities.User : manages
alms.Transaction ..> alms.Library : uses in process()
alms.persistence.FileManager ..> alms.Library : save/load

