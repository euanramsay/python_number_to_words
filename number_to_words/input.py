import convert_input
import sys

# Outputs the question to the terminal and takes in the user input and 
# checks to make sure it is an integer.

try:
	input = int(raw_input("What number would you like to convert to words? "))
except:
    print 'invalid'
    sys.exit()


print convert_input.convert_input_number(input)
	