class InsufficienntFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Cannot withdraw {amount}, Current Balance = {balance}"
        )
    
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficienntFundsError(balance, amount)
    return balance - amount
    
try:
    withdraw(100, 200)
except InsufficienntFundsError as e:
    print("InsufficientFundsError", e)
    