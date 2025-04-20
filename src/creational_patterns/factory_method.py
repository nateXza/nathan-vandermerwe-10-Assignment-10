from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} via Credit Card")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} via PayPal")