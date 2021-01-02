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

x = ["Now","We","are","cooking!","Hello"]
print(x)

print(x[1:3]) # start at index[1] end index(3 -1) = index[2]
print(x[:2]) # start at index[0], end at index(2 -1) = index[1]
print(x[2:]) # start at index[2], end till end of string
print(x[:])
print(x[::2]) # start at index[0], jump 1 positions

"""
The skip_elements function returns a list containing every other element from an input list,
 starting with the first element. Complete this function to do that, using the for loop to 
 iterate through the input list.
"""
def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0

	# Iterate through the list
	for i in elements:

		# Does this element belong in the resulting list?
		if element in new_list:
			# Add this element to the resulting list
			new_list.append(element[i])
			print(new_list)
		# Increment i
		i = i + 1
		#print(element)

	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

"""
Complete the skip_elements function to return every other element from the list, 
this time using the enumerate function to check if an element is on an even position
 or an odd position.
"""
def skip_elements(elements):
	# code goes here
	
	return ___

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


odd = []
for value in range(1,50):
  if value%2 == 0:
    continue
  odd.append(value)

odd.sort()
print(odd)