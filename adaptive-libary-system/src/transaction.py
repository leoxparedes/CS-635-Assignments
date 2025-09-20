class Transaction(X)
    def __init__(self, transaction_num, time):
        self._transaction_num
        self._time
    
    #Get transaction number
    def transaction_num(self):
        self._transaction_num
    #Get transaction time
    def time(self):
        self._time
    


class CheckoutOut(Transaction):
    def __init__(self, transaction_num, time):

class CheckedIn(Transaction):
    def __init__(self, transaction_num, time):
