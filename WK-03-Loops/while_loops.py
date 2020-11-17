# while loops
x = 0
while x < 5:
    print("Not there yet, x =" + str(x))
    x = x + 1
print("x = "+str(x))

#current = 1
def count_down(start_number):
  current = start_number  
  while (current > 0):
    print(current)
    current -= 1  #current = current -1
  print("Zero!")

count_down(3)

"""
Print prime numbers
A prime factor is a number that is prime and divides another without a remainder.
"""
def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor = factor + 1
  return "Done"
print_prime_factors(100)

"""
The multiplication_table function prints the results of a number passed to it multiplied 
by 1 through 5. An additional requirement is that the result is not to exceed 25, 
which is done with the break statement.
"""
def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = number * multiplier 
		# What is the additional condition to exit out of the loop?
		if result > 25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3)

"""
Print multiplication tables
"""
def multiplication_table(number,limit):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= limit:
		result = number * multiplier 
		# What is the additional condition to exit out of the loop?
		#if result > 25 :
		#	break
		print(str(number) + " x " + str(multiplier) + " = " + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3,10)