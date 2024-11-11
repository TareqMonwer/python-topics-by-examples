import abc


class PaymentMethodAbc(abc.ABC):
    @abc.abstractmethod
    def process_payment(self, amount: float):
        pass


class CreditCardPayment(PaymentMethodAbc):
    def process_payment(self, amount: float):
        print(f"Processing credit card payment of ${amount}")


class PayPalPayment(PaymentMethodAbc):
    def process_payment(self, amount: float):
        print(f"Processing PayPal payment of ${amount}")


class CryptoPayment(PaymentMethodAbc):
    def process_payment(self, amount: float):
        print(f"Processing cryptocurrency payment of ${amount}")


if __name__ == "__main__":
    def make_payment(payment_method: PaymentMethodAbc, amount: float):
        payment_method.process_payment(amount)

    # Using the different payment methods
    credit_card = CreditCardPayment()
    paypal = PayPalPayment()
    crypto = CryptoPayment()

    make_payment(credit_card, 100)  # Output: Processing credit card payment of $100
    make_payment(paypal, 200)       # Output: Processing PayPal payment of $200
    make_payment(crypto, 300)       # Output: Processing cryptocurrency payment of $300
