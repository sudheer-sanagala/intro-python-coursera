"""
String operations
len(string) Returns the length of the string
for character in string Iterates over each character in the string
if substring in string Checks whether the substring is part of the string
string[i] Accesses the character at index i of the string, starting at zero
string[i:j] Accesses the substring starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(string) by default.

String methods
string.lower() / string.upper() Returns a copy of the string with all lower / upper case characters
string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
string.count(substring) Returns the number of times substring is present in the string
string.isnumeric() Returns True if there are only numeric characters in the string. If not, returns False.
string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False.
string.split() / string.split(delimiter) Returns a list of substrings that were separated by whitespace / delimiter
string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.
delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter 
"""


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

# Strip method - removes white spaces, tab spaces
name = "SUdheer   "
print(name.strip())
print(name.upper())

# returns the no of times a character or word occurs
print(big_string.count("a"))
print(big_string.count("an"))

print(big_string.endswith("rope")) #True


# Join method - used to concatenate wors with a string sperated by space. It uses list of strings
join_var = " ".join(["This","is","a","senntence","joined","by","join","method"])
print(join_var)

join_var = "+".join(["This","is","a","senntence","joined","by","join","method"]) # join using + symbol
print(join_var)

# Split - This allows us to split a string into a list of strings.By default, it splits by any whitespace characters.
#  You can also split by any other characters by passing a parameter.
"This+is+a+senntence+joined+by+join+method"
print(join_var.split("+")) # the above string is split by the character specified into a list of strings

print("This is a senntence joined by join method".split())


def initials(phrase):
    words = phrase.split() # split into individual words
    print(words)
    result = ""
    for word in words:
        result += word[0] # extracts the first character of the string
    return result

print(initials("Universal Serial Bus"))