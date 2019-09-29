# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

def find_short(s):
    # your code here
    set_s = {len(x) for x in s.split()}
    l = min(set_s)
    return l

result = find_short("Hello Luca")
print(result)