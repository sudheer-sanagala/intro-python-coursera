"""
# Reverse a string
# string[start: end: step]
 S  U  D  H  E  E  R
 0  1  2  3  4  5  6
-7 -6 -5 -4 -3 -2 -1

-1 represents the last character of the string, -2 represents the second to last character and so on…
"""
my_string = 'SUDHEER'
print(my_string)
print(my_string[0:5]) # part of the string
print(my_string[:7])  # print till end of string
print(my_string[:])
print(my_string[-1:])
print(my_string[-5:]) # start from -5
print(my_string[-7:]) # start from -7
print(my_string[::2]) # print every 2nd character from string

print(my_string[::-1]) # reverse a string


print("--------------------")

for x in my_string:
    print("position - "+x)

print("--------------------")
#SUDHEER
# elements are added from left-to-right
val = ''
for x in my_string:
    val = x + val
    print("position - "+val)
print(val)

print("--------------------")