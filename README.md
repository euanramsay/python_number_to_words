# Number to Words Converter

This is a python program which takes in a number in digits between 0 and 999,999,999 and outputs the number in words.

e.g. input - 12, output - twelve  
input - 20500, output - twenty thousand five hundred

### Method

The program uses a method of treating numbers as having 3 sections - Millions,
Thousands and Sub-thousands. Each number entered is divided into those 3 sections.

e.g. 230500000  
Millions - 23  
Thousands - 500  
Sub-thousands - 0

Those numbers are then fed through the same algorithm to convert to words. 0 
values are disregarded. The words are then joined together with the appropriate 
'million', 'thousand' and 'and' strings to create the original large number as 
words.

e.g. twenty three million five hundred thousand

## Running the program

The program is started by running input.py within the folder number_to_words

## Testing

The unit tests can be run by running the file test.py from the folder tests