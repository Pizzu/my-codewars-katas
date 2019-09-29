# Given an array of one's and zero's convert the equivalent binary value to an integer.
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

def binary_array_to_number(arr):
   arr.reverse()
   result = 0
   for i in range(0,len(arr)):
      result += arr[i] * (2**i)
   return result

number = binary_array_to_number([1,0, 0, 0, 1])
print(number)