Class User:
    def __init__(self, name, email, redId, checkedOut, limit):
        self._ssname = name
        self._email = email
        self._redId = redId
        self._checkedOut = checkedOut
        self._limit = limit
    #Get user name
    def name(self):
        return self._name
    #Get email
    def email(self):
        return self._email
    #Get current amount of books checked out 
    def checkedOut(self):
        return self._checkedOut
    #Get limit of books able to be checked out 
    def limit(self):
        return self._limit
