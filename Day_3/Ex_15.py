from abc import ABC, abstractmethod

class PaymentProvider(ABC):
    @abstractmethod
    def process(self, amount):
        pass 

class CreditCard(PaymentProvider):
    def process(self, amount):
        print(f"Processing credit card payment: {amount} baht")

class BadProvider(PaymentProvider):
    pass  

cc = CreditCard()
cc.process(5000)

try:
    bad = BadProvider()
except TypeError as e:
    print("TypeError:", e)