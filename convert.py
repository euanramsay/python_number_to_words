import words

def number_to_words(number):
  
    if number == 0:
        return "Your number is zero"
    elif number < 0:
        return "Sorry, negative numbers are not allowed"
    elif 1 <= number <= 19:
        return words.small_numbers[number-1]
    elif 20 <= number <= 99:
        string = str(number)
        if string[1] == "0":
            return words.medium_numbers[int(string[0])-2]
        else:
            return words.medium_numbers[int(string[0])-2] + "-" + words.small_numbers[int(string[1])-1]
    elif 100 <= number <= 999:
        remainder = number % 100
        digit = number / 100
        if remainder == 0:
            return words.small_numbers[digit-1] + " hundred"
        else:
            return words.small_numbers[digit-1] + " hundred and " + number_to_words(remainder)