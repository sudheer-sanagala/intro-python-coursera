"""
String Arithmatic
"""
# multiply a string
val = "example"
print(val *3)

# adding to an existing string
print(val + "A")

# integers can be converted to str() type and concatenated to other strings
print(val + str(12.578))

#####################################################
"""
String index always starts from 0 and end with len(string) - 1
"""
name = 'JOHN DOE'

# first char of string
print(name[0]) #J

# last character of the name
print(name[7]) # len(name) - 1

"""
Slice = substring

[start:end:step]
:start - index of the string
:end - end index of string
The index [-1] would access the last character of the string, 
and the index [-2] would access the second-to-last character.
0  1  2  3  4  5
O  R  A  N  G  E

"""
fruit = "ORANGE"
print(fruit[1:4])
print(fruit[2:4])
print(fruit[1:5])


print(fruit[:2]) #index starts from 0 and ends with (2 - 1) index
print(fruit[2:]) #index starts from 2 and ends till end of string





big_string = 'Fantastic Mr.Fox jumps on a rope'