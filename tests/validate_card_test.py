from src.validation.validate_card import ValidateCard
import pytest


class TestCardValidation:

    validate_card = ValidateCard()

    ### Tests for Credit Card Number ###

    def test_empty_string_card_number(self):
        with pytest.raises(ValueError):
            self.validate_card.check_card_number("")

    def test_null_card_number(self):
        with pytest.raises(ValueError):
            self.validate_card.check_card_number(None)

    def test_less_than_16_digits_card_number(self):
        with pytest.raises(ValueError):
            self.validate_card.check_card_number("12345678")

    def test_greater_than_16_digits_card_number(self):
        with pytest.raises(ValueError):
            self.validate_card.check_card_number("12345678901234567890")

    def test_special_char_card_number(self):
        with pytest.raises(ValueError):
            self.validate_card.check_card_number("123456%8901234$#")

    def test_16_digit_card_number(self):
        assert 0 == self.validate_card.check_card_number("1234567890123456")

    def test_numeric_arg_card_number(self):
        with pytest.raises(ValueError):
            self.validate_card.check_card_number(1234567890123456)


    ### Tests for Card Holder ###
    
    def test_empty_string_card_holder(self):
        with pytest.raises(ValueError):
            self.validate_card.check_card_holder("")
        
    def test_null_card_holder(self):
        with pytest.raises(ValueError):
            self.validate_card.check_card_holder(None)

    def test_numeric_arg_card_holder(self):
        with pytest.raises(ValueError):
            self.validate_card.check_card_holder(1234)

    def test_special_char_card_holder(self):
        with pytest.raises(ValueError):
            self.validate_card.check_card_holder("de#jong")

    
    ### Tests for Expiration Date ###

    def test_empty_datetime(self):
        with pytest.raises(ValueError):
            self.validate_card.check_expiration_date([])

    def test_null_datetime(self):
        with pytest.raises(ValueError):
            self.validate_card.check_expiration_date(None)

    def test_month_out_of_range_datetime(self):
        with pytest.raises(ValueError):
            self.validate_card.check_expiration_date([2021, 13, 8])

    def test_date_out_of_range_datetime(self):
        with pytest.raises(ValueError):
            self.validate_card.check_expiration_date([2021, 4, 32])

    def test_past_datetime(self):
        with pytest.raises(ValueError):
            self.validate_card.check_expiration_date([2021,1,10])

    def test_negative_year_datetime(self):
        with pytest.raises(ValueError):
            self.validate_card.check_expiration_date([-2021, 3, 12])

    def test_negative_month_datetime(self):
        with pytest.raises(ValueError):
            self.validate_card.check_expiration_date([2021, -6, 31])

    def test_negative_day_datetime(self):
        with pytest.raises(ValueError):
            self.validate_card.check_expiration_date([2022, 11, -2])

    def test_jumbled_input_datetime(self):
        with pytest.raises(ValueError):
            self.validate_card.check_expiration_date([12, 5, 2022])

    def test_valid_datetime(self):
        assert 0 == self.validate_card.check_expiration_date([2022, 2, 17])

    
    ### Tests for Security Code ###

    def test_empty_security_code(self):
        with pytest.raises(ValueError):
            self.validate_card.check_security_code("")

    def test_null_security_code(self):
        assert 0 == self.validate_card.check_security_code(None)

    def test_less_than_3_digits_security_code(self):
        with pytest.raises(ValueError):
            self.validate_card.check_security_code("12")

    def test_greater_than_3_digits_security_code(self):
        with pytest.raises(ValueError):
            self.validate_card.check_security_code("3344")

    def test_special_char_security_code(self):
        with pytest.raises(ValueError):
            self.validate_card.check_security_code("1*3")

    def test_numeric_arg_security_code(self):
        with pytest.raises(ValueError):
            self.validate_card.check_security_code(567)

    def test_valid_3_digit_security_code(self):
        assert 0 == self.validate_card.check_security_code("434")

    
    ### Tests for Amount ###

    def test_null_amount(self):
        with pytest.raises(ValueError):
            self.validate_card.check_amount(None)

    def test_positive_integer_amount(self):
        with pytest.raises(ValueError):
            self.validate_card.check_amount(322)

    def test_negative_integer_amount(self):
        with pytest.raises(ValueError):
            self.validate_card.check_amount(-98)

    def test_string_amount(self):
        with pytest.raises(ValueError):
            self.validate_card.check_amount("568.99")

    def test_negative_float_amount(self):
        with pytest.raises(ValueError):
            self.validate_card.check_amount(-34.99)

    def test_positive_float_amount(self):
        assert 0 == self.validate_card.check_amount(72.55)