Class Book:
    def __init__(self, book_name, author, isbn, stock, full_stock):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__stock = stock
    #Get book title
    def title(self):
        return self._title
    #Get book author
    def author(self):
        return self.__author
    #Get book isbn
    def isbn(self):
        return self.__isbn
    #Get current stock
    def stock(self):
        return self.__stock
    #Get full amount of books when all checked in 
    def full_stock(self):
        return self.__full_stock
