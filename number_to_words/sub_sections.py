import convert

def decide_sections(section):
	"""
	Takes a number representing one of the three sections of the number from
	1 to 999,999,999 and if the number is 0 does not convert it to words, if the
	number has a value it is converted to words.
	"""
	if section == 0:
		return ""
	else:
		return convert.number_to_words(section)