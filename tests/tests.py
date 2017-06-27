import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from number_to_words import convert_input

class TestStringMethods(unittest.TestCase):

    def test_convert_single_digit(self):
        self.assertEqual(convert_input.convert_input_number("3"), "three")

    def test_convert_double_digit(self):
        self.assertEqual(convert_input.convert_input_number("21"), "twenty one")

    def test_convert_hundred(self):
        self.assertEqual(convert_input.convert_input_number("105"), "one hundred and five")

    def test_convert_large_number(self):
        self.assertEqual(convert_input.convert_input_number("56945781"), "fifty six million nine hundred and forty five thousand seven hundred and eighty one")

    def test_convert_large_number_with_extra_and_before_small_number(self):
        self.assertEqual(convert_input.convert_input_number("10001"), "ten thousand and one")

    def test_convert_number_with_all_same_digits(self):
        self.assertEqual(convert_input.convert_input_number("2222222"), "two million two hundred and twenty two thousand two hundred and twenty two")

    def test_convert_zero(self):
        self.assertEqual(convert_input.convert_input_number("0"), "zero")

    def test_convert_negative_number(self):
        self.assertEqual(convert_input.convert_input_number("-1"), "invalid")

    def test_convert_out_of_range_number(self):
        self.assertEqual(convert_input.convert_input_number("1000000000"), "invalid")

    def test_convert_a_string(self):
        self.assertEqual(convert_input.convert_input_number("twenty"), "invalid")

    def test_convert_a_number_with_decimal_point(self):
        self.assertEqual(convert_input.convert_input_number("5.6"), "invalid")

    

if __name__ == '__main__':
    unittest.main()


