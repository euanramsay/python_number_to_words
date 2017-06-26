import convert

def decide_sections(section):
	if section == 0:
		return ""
	else:
		return convert.number_to_words(section)