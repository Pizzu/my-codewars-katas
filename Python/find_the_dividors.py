# Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

# Example:
# divisors(12); #should return [2,3,4,6]
# divisors(25); #should return [5]
# divisors(13); #should return "13 is prime"

def divisors(integer):
   if is_prime(integer):
      return str(integer) + " is prime"
   else:
      divisors = [num for num in range(2,integer) if integer % num == 0]
      return divisors


def is_prime(num):
   if num >= 2:
      for n in range(2,num):
         if num % n == 0:
            return False
      return True
   else:
      return False

result = divisors(2)
print(result)