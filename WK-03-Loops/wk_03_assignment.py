"""
The even_numbers function returns a space-separated string of all positive numbers that are divisible by 2,
up to and including the maximum that's passed into the function. For example, even_numbers(6) returns “2 4 6”. 
Fill in the blank to make this work.
"""
def even_numbers(maximum):
	return_string = ""
	for x in ___:
		return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed

"""
The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise. 
"""
def counter(start, stop):
	x = start
	if ___:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if ___:
				return_string += ","
			___
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if ___:
				return_string += ","
			___
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"


"""
Question 4
This function prints out a multiplication table (where each number is the result of multiplying
the first number of its row by the number at the top of its column). Fill in the blanks so that calling multiplication_table(1, 3) 
will print out:

1 2 3

2 4 6

3 6 9
"""
def multiplication_table(start, stop):
	for x in range(start):
		for y in range(stop):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)

"""

"""