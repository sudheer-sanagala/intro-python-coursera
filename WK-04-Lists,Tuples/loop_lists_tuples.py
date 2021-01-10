
animals = ["lion","zebra","monkey"]
print(len(animals)) # number of elements on the list

chr = 0
for animal in animals:
    print(animal)   # loop through list
    chr = chr + len(animal)

print(f"Total characters in the list {chr}, Average length {chr/len(animals)}!")


# Enumerate function returns the position and value. Enumerate returns tuple
for idx, val in enumerate(animals):
    print(f'Index {idx} contains {val} in the list!')


# print every other element
def skip_elements(elements):
    for pos, val in enumerate(elements):

        if pos%2==0:
            print(val)
    return val

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))


# unpack tuple. Here people is a tuple
def full_email(people):
    result = [] # empty list
    for email, name in people:
        result.append(name + ' '+ email)

    return result
print(full_email([("testa.com","sudheer"),("testb.com","sanagala")])) # pass a list of tuples