
list_1 = ['head', 'ears', 3, 'legs', 5.8]
#print(type(list_1))
print(list_1)

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