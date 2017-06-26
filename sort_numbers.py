import sub_sections

def section_numbers(number):
	millions = number / 1000000
	sub_thousands = number % 1000
	thousands = (number % 1000000 - sub_thousands) / 1000

	first = sub_sections.decide_sections(millions)
	second = sub_sections.decide_sections(thousands)
	third = sub_sections.decide_sections(sub_thousands)

	if (first or second) and (sub_thousands < 100):
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