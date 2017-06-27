import sort_numbers

def convert_input_number(number):
	"""
	Checks the validity of the number entered to make sure it is within
	the limit of 999,999,999 and is not negative. 
	"""
	if number == 0:
		return "zero"
	elif number < 0:
		return "invalid"
	elif number > 999999999:
		return "invalid"
	else:
		return sort_numbers.section_numbers(number)