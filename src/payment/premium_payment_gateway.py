from src.payment.payable import Payable

class PremiumPaymentGateway(Payable):

    def pay(self, amount):
        return "Paid with Premium Payment Gateway"