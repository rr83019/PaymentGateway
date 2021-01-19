import logging
from src.payment.expensive_payment_gateway import ExpensivePaymentGateway
from src.payment.premium_payment_gateway import PremiumPaymentGateway
from src.payment.cheap_payment_gateway import CheapPaymentGateway
from retry import retry

class PaymentProvider:

    def process_payment(self, amount):

        if amount <= 20 and amount > 0:
            result = self.pay_with_cheap_gateway(amount)
            
        elif amount > 20 and amount <= 500:
            try:
                result = self.pay_with_expensive_gateway(amount)
            except Exception as e:
                logging.error("error: {}".format(e))
                result = self.pay_with_cheap_gateway(amount)
            
        elif amount > 500:
            result = self.pay_with_premium_gateway(amount)
        
        else:
            raise ValueError("Invalid amount: {}".format(amount))

        return result

    
    def pay_with_cheap_gateway(self, amount):
        provider = CheapPaymentGateway()
        return provider.pay(amount)

    def pay_with_expensive_gateway(self, amount):
        provider = ExpensivePaymentGateway()
        return provider.pay(amount)

    @retry(tries=3)
    def pay_with_premium_gateway(self,amount):
        provider = PremiumPaymentGateway()
        return provider.pay(amount)
