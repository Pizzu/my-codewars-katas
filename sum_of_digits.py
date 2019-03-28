# In this kata, you must create a digital root function.

# A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

# Here's how it works:

# digital_root(16)
# => 1 + 6
# => 7

# digital_root(942)
# => 9 + 4 + 2
# => 15 ...
# => 1 + 5
# => 6

def digital_root(n):
    digit_list = [int(d) for d in str(n)]
    if len(digit_list) == 1:
      return digit_list[0]
    else:
        return digital_root(sum(digit_list))

print(digital_root(166))