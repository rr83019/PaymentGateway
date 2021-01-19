from datetime import datetime

class ValidateCard:

    def check_card_number(self, number):
        if not isinstance(number, str) or len(number) != 16 or not number.isnumeric():
            raise ValueError("Invlaid credit card number: {}".format(number))
        return 0

    def check_card_holder(self, holder):
        if not isinstance(holder, str) or len(holder) == 0 or not all(x.isalpha() or x.isspace() for x in holder):
            raise ValueError("Invalid input for card holder: {}".format(holder))
        return 0

    def check_expiration_date(self, date):
        try:
            exp_date = datetime(date[0], date[1], date[2])
        except Exception:
            raise ValueError("Ivalid expiration date format: {}".format(date))

        if not isinstance(exp_date, datetime) or exp_date < datetime.today():
            raise ValueError("Invalid expiration date: {}".format(date))
        return 0

    def check_security_code(self, code):
        if code is not None:
            if not isinstance(code, str) or len(code) != 3 or not code.isnumeric():
                raise ValueError("Invalid security code: {}".format(code))
        return 0

    def check_amount(self, amount):
        if not isinstance(amount, float) or amount < 0:
            raise ValueError("Invalid amount: {}".format(amount))
        return 0