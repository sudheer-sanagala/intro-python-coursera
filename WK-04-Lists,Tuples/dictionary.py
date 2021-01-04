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