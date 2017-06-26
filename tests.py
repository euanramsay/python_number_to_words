import unittest
import convert_input

class TestStringMethods(unittest.TestCase):

    def test_convert_single_digit(self):
        self.assertEqual(convert_input.convert_input_number(3), "three")

    def test_convert_double_digit(self):
        self.assertEqual(convert_input.convert_input_number(21), "twenty-one")

    def test_convert_hundred(self):
        self.assertEqual(convert_input.convert_input_number(105), "one hundred and five")

    def test_convert_large_number(self):
        self.assertEqual(convert_input.convert_input_number(56945781), "fifty-six million nine hundred and forty-five thousand seven hundred and eighty-one")

    def test_convert_zero(self):
        self.assertEqual(convert_input.convert_input_number(0), "zero")

    def test_convert_negative_number(self):
        self.assertEqual(convert_input.convert_input_number(-1), "Sorry, negative numbers are not allowed")

    def test_convert_out_of_range_number(self):
        self.assertEqual(convert_input.convert_input_number(1000000000), "Sorry, only numbers up to 999,999,999 allowed")

    def test_convert_large_number_with_extra_and_before_small_number(self):
        self.assertEqual(convert_input.convert_input_number(10001), "ten thousand and one")

    def test_convert_number_with_all_same_digits(self):
        self.assertEqual(convert_input.convert_input_number(2222222), "two million two hundred and twenty-two thousand two hundred and twenty-two")

if __name__ == '__main__':
    unittest.main()


