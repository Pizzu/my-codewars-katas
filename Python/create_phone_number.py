# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# Example:
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge. 
# Don't forget the space after the closing parentheses!

#One possible solution
def create_phone_number(n):
    arr_str = [str(num) for num in n]
    prefix = "".join(arr_str[0:3])
    first_part = "".join(arr_str[3:6])
    last_part = "".join(arr_str[6:len(arr_str)])
    return "(" + prefix + ") " + first_part + "-" + last_part

#Clever solution
def create_phone_numbers(n):
  return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)