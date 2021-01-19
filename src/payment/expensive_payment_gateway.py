from src.payment.payable import Payable

class ExpensivePaymentGateway(Payable):

    def pay(self, amount):
        return "Paid with Expensive Payment Gateway"