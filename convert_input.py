import sort_numbers

def convert_input_number(number):
	if number == 0:
		return "zero"
	elif number < 0:
		return "Sorry, negative numbers are not allowed"
	elif number > 999999999:
		return "Sorry, only numbers up to 999,999,999 allowed"
	else:
		return sort_numbers.section_numbers(number)