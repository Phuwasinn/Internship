class Account:
    def __init__(self, balance):
        self.__balance = balance

acc = Account(1000)
try:
    print(acc.balance)
except AttributeError as e:
    print("Attribute Error:", e)

print("Correct way:", acc._account__balance)