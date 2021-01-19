import logging
from payment.payment_provider import PaymentProvider
from validation.validate import validate
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/processpayment', methods=['POST'])
@validate
def process_payment():
    request_data = request.get_json()
    payment_provider = PaymentProvider()

    try:
        payment_provider.process_payment(request_data['Amount'])
        message = "OK"
        status_code = 200
    except Exception as e:
        logging.error("error: {}".format(e))
        message = "Internal Server Error"
        status_code = 500

    return jsonify({"data":message}), status_code
