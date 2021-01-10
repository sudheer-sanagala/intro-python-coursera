# These are immutable sequences of objects enclosed by parentheses ()
# immutable means, once created a tuple, they cannot be modified

tuple_1 = (3, 'bags', 'belt', 2020, 7.9)
tuple_2 = (1,4,6,2)

# Tuples are indexed like lists, so values can be extracted by specifying index
print(tuple_1[1])
print(tuple_1[0])
print(tuple_1[2:-1])

print('backpack' in tuple_1)
print(len(tuple_1))
print(max(tuple_2))


# A dictionary is an unordered collection of key-value pairs enclosed by curly braces {}. 
# Dictionaries are useful for storing information in pairs of ‘keys’ and ‘values’.
dict_2 = {'fruits': ['apple','grape'],
           10     : 'number of fruits',
         'carrier': 'bag'}
print(dict_2)

print(dict_2['fruits'])
print(dict_2[10])


# append a value to a dict. It adds at the end
dict_2['fruits'].append("banana")
print(dict_2)

# update a value to a dict
dict_2['carrier'] = 'basket'
print(dict_2)

# add a new value to dict
dict_2['status'] = 'not enough'
print(dict_2)


print('-------------------------------')
print(dict_2.keys())
print(dict_2.values())


def file_size(file_info):
    name, type, size= file_info
	  return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21



animals = ["lion","zebra","monkey"]
print(len(animals))