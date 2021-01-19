from src.payment.payable import Payable

class CheapPaymentGateway(Payable):

    def pay(self, amount):
        return "Paid with Cheap Payment Gateway"