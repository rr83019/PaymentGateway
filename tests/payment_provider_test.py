from src.payment.payment_provider import PaymentProvider
import pytest

class TestPaymentProvider:

    provider = PaymentProvider()

    def test_amount_less_than_20(self):
        assert "Paid with Cheap Payment Gateway" == self.provider.process_payment(19.99)

    def test_amount_between_21_500(self):
        assert "Paid with Expensive Payment Gateway" == self.provider.process_payment(255.65)

    def test_amount_greater_than_500(self):
        assert "Paid with Premium Payment Gateway" == self.provider.process_payment(777.123)

    def test_amount_less_than_0(self):
        with pytest.raises(ValueError):
            self.provider.process_payment(-33.39)