# CS 635 Project 1: Adaptive Library Management System (ALMS)

## Contributors: Leo Paredes, Brandon Reynolds

# Getting started...
At the root directory enter the following in the terminal window.
1) python -m venv .venv
2) .venv\Scripts\activate
3) pip install pytest


# How to run pytest...
All tests for ALMS can be found in "test_suites/". To run tests, enter "pytest" in the terminal window. Pytest session will start, collect all tests, run all tests, and report PASS/FAIL. 

# Demo
A demo of the ALMS can be found in "main.py". To execute the demo, enter "python main.py" in the terminal window. 

# UML Diagram 

```mermaid
classDiagram
direction LR
class Library {
  +add_book(b: Book)
  +add_user(u: User)
  +get_book(isbn: str): Book?
  +get_user(uid: str): User?
  +search_books(q: str): Book[]
  +search_users(q: str): User[]
  +borrow_book(uid: str, isbn: str): bool
  +return_book(uid: str, isbn: str): bool
  +to_dict(): dict
  +from_dict(data: dict) Library
}
class Searchable { <<interface>> +matches(text: str): bool }
class Transaction { <<abstract>> +user_id: str +isbn: str +process(lib: Library) bool }
class BorrowTransaction { +process(lib: Library) bool }
class ReturnTransaction { +process(lib: Library) bool }

BorrowTransaction --|> Transaction
ReturnTransaction --|> Transaction
Transaction ..> Library : process()


```mermaid
classDiagram
direction LR
class BaseEntity { -_identifier: str +get_id(): str +to_dict(): dict }

class Book {
  -_isbn: str
  -_title: str
  -_author: str
  -_total_copies: int
  -_available_copies: int
  +is_available(): bool
  +borrow_one(): bool
  +return_one(): bool
  +matches(text: str): bool
  +to_dict(): dict
  +from_dict(data: dict) Book
}

class User {
  -_user_id: str
  -_name: str
  -_email: str
  -_borrowed_isbns: str[]
  +borrow_isbn(isbn: str)
  +return_isbn(isbn: str) bool
  +matches(text: str): bool
  +to_dict(): dict
  +from_dict(data: dict) User
}

class Searchable { <<interface>> +matches(text: str): bool }

Book --|> BaseEntity
User --|> BaseEntity
Book ..|> Searchable
User ..|> Searchable

```mermaid
classDiagram
direction LR
class FileManager { +file_path: str +save(lib: Library) +load(library_class) Library }

class BookNotFoundError
class UserNotFoundError
class BookNotAvailableError
class TransactionError

FileManager ..> Library : save/load
BookNotFoundError --|> Exception
UserNotFoundError --|> Exception
BookNotAvailableError --|> Exception
TransactionError --|> Exception