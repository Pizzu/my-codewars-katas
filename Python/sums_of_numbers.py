# Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!

def get_sum(a,b):
    #good luck!
    if a == b:
        return a
    if b < a:
        result = sum_range(b,a)
        return result
    else:
        result = sum_range(a,b) 
        return result
        
        
def sum_range(a,b):
    sum = 0
    for num in range(a,b+1):
            sum = sum + num
    return sum