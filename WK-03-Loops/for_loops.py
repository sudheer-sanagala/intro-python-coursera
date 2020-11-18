"""
loops start with 0th element
"""

for x in range(5):
    print(x)


friends = ['rama','sudheer','chaitu']
for friend in friends:
    print("Hi "+friend)

# for loop over a list
# sum a list of numbers
values = [2,4,5,8,100,500]
sum, length = 0,0
for value in values:     # iterate over each element in the list   
    sum = sum + value    # adding current values to sum of the list
    length = length + 1  # calculates how many in the list

print("Sum of Numbers "+str(sum)+" Avg "+ str(sum/length))

# sum of numbers in a range
product = 1
for n in range(1, 10):
    product = product * n
    print("Product "+str(product *n))

print("Total Sum "+str(product))

# factorial of a number
def factorial(n):
    result = 1
    for i in range(result,n + result):
        print("varable - "+str(i))
        result = result*i
        print("Inside result - " + str(result))
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

# my factorial
def my_factorial(n):
    result = 1
    for i in range(result,n + result):
        result = n *my_factorial(n-1)

    return result

print(my_factorial(4)) # should return 24
print(my_factorial(5)) # should return 120

# range function with `step` parameter
def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print(x, to_celsius(x))

# print sum of numbers
for x in range(10,40,5):
    print("Here -"+ str(x * 2))

# Nested loops
players = ['Sachin','Dravid','Kohli','Dhoni']
for first_player in players:
    for contender in players:
        if first_player != contender:
            print(first_player+ " VS " +contender)


# loop through each character in the string
my_str = 'Sudheer'
for i in my_str:
    print("Value :"+str(i))


# loop though each value in the list
my_list = ['Red','Green','Yellow']
for x in my_list:
    print("Elements in list : "+x)


# numbers should be included in the range
my_number = 10
for i in range(my_number):
    print("Element "+str(i))


# loop through between a range
my_max_range = 20
my_min_range = 10
for i in range(my_min_range,my_max_range):
    print("Element : "+str(i))

# loop in reverse
for i in range(10, -6, -2):
    print(i)

# reverse a list
#start -> length of a list -1
#end -> -1
#step -> -1
list = ['Mon', 'Tue', 'Wed', 'Thu']
for i in range(len(list) - 1, -1, -1): 
   print(list[i])    