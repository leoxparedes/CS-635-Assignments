## UML — Core (Library, Transactions, Searchable)

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


```markdown
## UML — Entities (Book, User, BaseEntity)

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

%% Re-declare Searchable for this block
class Searchable { <<interface>> +matches(text: str): bool }

Book --|> BaseEntity
User --|> BaseEntity
Book ..|> Searchable
User ..|> Searchable



```markdown
## UML — Persistence & Exceptions

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
