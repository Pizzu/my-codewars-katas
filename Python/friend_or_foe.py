# Make a program that filters a list of strings and returns a list with only your friends name in it.
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
# Note: keep the original order of the names in the output.

people = ["Ryan", "Kieran", "Jason", "Yous"]

def friend(arr):
   my_friends = list(filter(lambda x: len(x) == 4, arr))
   return my_friends

result = friend(people)
print(result)