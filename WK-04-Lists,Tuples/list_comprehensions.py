from typing import MutableMapping



# Print multiples of 7
multiples = []
for x in range(1,11):
    #append to the list
    multiples.append(x*7)

print(multiples)

#using list comprehension
multiples = [ x*7 for x in range(1,11)]
print(multiples)

# print lengths of the languages in the list
languages = ["python","java","ruby","javascript"]
lengths = [len(language) for language in languages]
print(lengths)

# using regualar for loop over string
lengths = []
for language in languages:
    lengths.append(len(language))
print(lengths)

# print multiples of 3 less than 100
z= []
z = [x for x in range(1,101) if x%3 == 0]
print(z)

# print odd numbers in the list
def odd_numbers(n):
    """
    docstring
    """
    return [x for x in range(1,n+1) if x%2 != 0]

print(odd_numbers(5))
print(odd_numbers(10))
print(odd_numbers(1))
print(odd_numbers(-1))

# print cubes of a number from 1 to 10
c = []
c = [x**3 for x in range(1,11) ]
print(c)