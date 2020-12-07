## List are created with square brackets [ ]. List are mutable, which means, the values of the list can be updated.

list_1 = ['head', 'ears', 3, 'legs', 5.8]
#print(type(list_1))
print(list_1)
#print(list_1.reverse)

# add elements to the list. `append` always adds new element at the end
list_1.append("Hello")
print(list_1)

list_1.append(33.56)
print(list_1)


# remove elements from the list
list_1.remove("ears")
print(list_1)


# update an element in the list by specifying the index. It overwrites the exising value in the list
# if the index is not available, it will throw an out of index error
list_1[2] = 'new'
print(list_1)

#list_1[10] = 'Sudheer' Index out of bounds
#print(list_1)
print("-------------------")
print(list_1[0]) #first element
print(list_1[:]) #all the elements
print(list_1[2:4]) # from 3rd element to but not including 5th
print(list_1[-1]) #last element
print(list_1[1:-1]) #2nd element to but not including last

# multiply a list, it can include integers and strings
a = [1,2,3]
print(a * 3)

b = [4,5,"Hello"]
print(b * 2)

c = ['S','U']
print(c*3)


# Check element in the list


# loop through a list
for i in list_1:
    print(i)