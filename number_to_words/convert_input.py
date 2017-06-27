import words

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
		return section_numbers(number)

def decide_sections(section):
	"""
	Takes a number representing one of the three sections of the number from
	1 to 999,999,999 and if the number is 0 does not convert it to words, if the
	number has a value it is converted to words.
	"""
	if section == 0:
		return ""
	else:
		return number_to_words(section)

def number_to_words(number):
    """
    Takes in a number between 1 and 999 and returns the number in words.
    """
    if 1 <= number <= 19:
        return words.small_numbers[number-1]
    elif 20 <= number <= 99:
        string = str(number)
        if string[1] == "0":
            return words.medium_numbers[int(string[0])-2]
        else:
            return words.medium_numbers[int(string[0])-2] + " " + words.small_numbers[int(string[1])-1]
    elif 100 <= number <= 999:
        remainder = number % 100
        digit = number / 100
        if remainder == 0:
            return words.small_numbers[digit-1] + " hundred"
        else:
            return words.small_numbers[digit-1] + " hundred and " + number_to_words(remainder)

def section_numbers(number):
	"""
	Takes a number from 1 to 999,999,999 and divides it up into 3 smaller numbers.
	One number representing the millions, one representing the thousands and one 
	representing the sub-thousands numbers.
	First, second and third variables are creating representing the three sections
	of the number as it appears on the page.
	The function then puts these strings together to create the structure of the
	number as words.
	"""
	millions = number / 1000000
	sub_thousands = number % 1000
	thousands = (number % 1000000 - sub_thousands) / 1000

	first = decide_sections(millions)
	second = decide_sections(thousands)
	third = decide_sections(sub_thousands)

	if (first or second) and (sub_thousands < 100) and (sub_thousands != 0):
		small_and = "and "
	else:
		small_and = ""

	if first:
		million = " million "
	else:
		million = ""

	if second:
		thousand = " thousand "
	else:
		thousand = ""

	return first + million + second + thousand + small_and + third
	