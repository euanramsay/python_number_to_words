import sort_numbers

def convert_input_number(raw_number):
	"""
	Checks the validity of the number entered. 
	First checks to make sure the number is a valid integer, converting raw string 
	to int if there if an error 'invalid' is output.
	If number is 0, 'zero' is output.
	If number is negtive or over the limit of 999,999,999 "invalid" is output.
	If all passes calls section_numbers function on the number. 
	"""
	try:
		number = int(raw_number)
	except:
	    return 'invalid'

	if number == 0:
		return "zero"
	elif number < 0:
		return "invalid"
	elif number > 999999999:
		return "invalid"
	else:
		return sort_numbers.section_numbers(number)