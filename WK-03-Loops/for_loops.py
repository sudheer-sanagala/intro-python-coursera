for x in range(5):
    print(x)


friends = ['rama','sudheer','chaitu']
for friend in friends:
    print("Hi "+friend)

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
for x in range(10,40):
    print("Here -"+ str(x * 2))
    