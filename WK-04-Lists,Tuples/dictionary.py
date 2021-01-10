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