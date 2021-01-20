"""
x = {key1:value1, key2:value2} 

Operations

len(dictionary) - Returns the number of items in the dictionary
for key in dictionary - Iterates over each key in the dictionary
for key, value in dictionary.items() - Iterates over each key,value pair in the dictionary
if key in dictionary - Checks whether the key is in the dictionary
dictionary[key] - Accesses the item with key key of the dictionary
dictionary[key] = value - Sets the value associated with key
del dictionary[key] - Removes the item with key key from the dictionary
Methods

dict.get(key, default) - Returns the element corresponding to key, or default if it's not present
dict.keys() - Returns a sequence containing the keys in the dictionary
dict.values() - Returns a sequence containing the values in the dictionary
dict.update(other_dictionary) - Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.
dict.clear() - Removes all the items of the dictionary
"""


# Create a new dictionary
tech_dictionary = {
    "React": "Library for building user interfaces.",
    "Node": "JavaScript runtime.",
    "C#": "Strongly typed programming language",
}

# Read
print(tech_dictionary["Node"]) # "JavaScript runtime."

# Check if key exists
if "Java" in tech_dictionary:
  print('Java is in dictionary!')

# Change item value
tech_dictionary["React"] = "Popular frontend library"

# Add item
tech_dictionary["Python"] = "Most famous programming language in 2020"

# Remove item
tech_dictionary.pop("C#")

file_counts = {"jpg":10, "txt":15, "csv":20}
print(file_counts)
print(file_counts["csv"])

print("jpg" in file_counts) # check jpg exists in dictionary
print("html" in file_counts) # html does not exists in dictionary

# add new dictionary value
file_counts["cfg"] = 8
print(file_counts)

# update an existing dictionary value
# Before update - {'jpg': 10, 'txt': 15, 'csv': 20, 'cfg': 8}
# After update - {'jpg': 10, 'txt': 15, 'csv': 10, 'cfg': 8}
file_counts["csv"] = 10
print(file_counts)

# delete a key from dictionary
#del file_counts["cfg2"] # if key does not exist it will return KeyError: 'cfg2'
del file_counts["cfg"]
print(file_counts)

# loop through a dictionary
for ext, amount in file_counts.items():
    print(f'There are {amount} files with extension {ext}')

# default prints keys
for extensions in file_counts:
  print(extensions)

# to print values
for val in file_counts.values():
  print(val)


# count the letters in a sentence
def count_letters(text):
  result = {} # define a empty dictionary

  # loop through each letter in the text
  for letter in text:

    # add to dictionary - add KEY(letter) and set VALUE to 0 for first time
    # check the letter is in dictionary, if not then add it
    if letter not in result:
      result[letter] = 0
    
    # if the KEY(letter) is found in dictionary then increment the VALUE of that KEY(letter)
    result[letter] += 1

  for let,cnt in result.items():
    print(f'There are {cnt} for charcter {let}')
  return result

print(count_letters("this is a sample text"))

# Dictionary can contain list as value
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for __:
	for __:
		print("{} {}".format(__))