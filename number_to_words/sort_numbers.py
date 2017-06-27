import sub_sections

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

	first = sub_sections.decide_sections(millions)
	second = sub_sections.decide_sections(thousands)
	third = sub_sections.decide_sections(sub_thousands)

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