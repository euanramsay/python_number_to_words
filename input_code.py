import sort_numbers


number = input("What number would you like to convert to words? ")

if number == 0:
    print "Your number is zero"
elif number < 0:
    print "Sorry, negative numbers are not allowed"
elif number > 999999999:
	print "Sorry, only numbers up to 999,999,999 allowed"
else:
	print sort_numbers.section_numbers(number)