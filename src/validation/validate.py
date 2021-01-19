from functools import wraps
from flask import jsonify, request
import logging
from validation.validate_card import ValidateCard

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
validate_card = ValidateCard()

def validate(f):
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            data = request.get_json()
            validate_payment_args(data)
        except ValueError as e:
            logging.error("error: {}".format(e))
            return jsonify({"error":"Bad request"}), 400
        except Exception as e:
            logging.error("error: {}".format(e))
            return jsonify({"error": "Internal Server Error"}), 500
        return f(*args, **kw)
    return wrapper


def validate_payment_args(data):
    try:
        card_number = data['CreditCardNumber']
        card_holder = data['CardHolder']
        expiration_date = data['ExpirationDate']
        try:
            security_code = data['SecurityCode']
        except:
            security_code = None
        amount = data['Amount']

        validate_card.check_card_number(card_number)
        validate_card.check_card_holder(card_holder)
        validate_card.check_expiration_date(expiration_date)
        validate_card.check_security_code(security_code)
        validate_card.check_amount(amount)

    except (ValueError, KeyError) as e:
        raise ValueError(e)
    except Exception as e:
        raise Exception(e)