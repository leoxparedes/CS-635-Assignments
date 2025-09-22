#Overall Library system error
class LibraryError(Exception):
    pass

#Out of stock error
class BookUnavailableError(LibraryError):
    pass

#User not found error
class UserNotFoundError(LibraryError):
    pass

#Transaction error when check in/out is not working
class TransactionError(LibraryError):
    pass
