# Define a function isPrime/is_prime() that takes one integer argument and returns true/True or false/False depending on if the integer is a prime.

# Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.


def is_prime(num):
   if num >= 2:
      for n in range(2,num):
         if num % n == 0:
            return False
      return True
   else:
      return False

result = is_prime(10)
print(result)