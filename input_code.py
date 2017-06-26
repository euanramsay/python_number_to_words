import convert


number = input("What number would you like to convert to words? ")


millions = number / 1000000
sub_thousands = number % 1000
thousands = (number % 1000000 - sub_thousands) / 1000

if millions == 0:
	first = ""
else:
	first = convert.number_to_words(millions)

if thousands == 0:
	second = ""
else:
	second = convert.number_to_words(thousands)

if sub_thousands == 0:
	third = ""
else:
	third = convert.number_to_words(sub_thousands)


print millions
print thousands
print sub_thousands
print first + " million " + second + " thousand " + third

# print convert.number_to_words(number)

# def number_to_word(number):


# length = len(str(number))


# print "Your number is: ", number
# print "It is ", length, " digits long"

# if number == 0:
# 	print "Your number is zero"
# elif number < 0:
# 	print "Sorry, negative numbers are not allowed"
# elif length >= 1 and length <= 3:
# 	print "Your number is less than a thousand"
# elif length >= 4 and length <= 6:
# 	print "Your number is less than a million"
# elif length >= 7 and length <= 9:
# 	print "Your number is less than a billion"
# else:
# 	print "Sorry, numbers over 999,999,999 are not allowed"


# print "You number in words is: ", words.small_numbers[number-1]

# digit_array = [int(digit) for digit in str(number)]

# print digit_array

# length_of_array = len(digit_array)
# small_digits = digit_array[length_of_array-1]

# print small_digits
