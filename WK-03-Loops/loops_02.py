no_of_lines = 10
symbol = '*'
star = ''
for i in range(no_of_lines):
    star = star + symbol
    print(star)

# print in reverse
for x in range(no_of_lines):
    star = no_of_lines
    no_of_lines = no_of_lines - 1
    print(star * symbol)


print("Here is a scarf")
print('~#'*10)
print('#-'*10)
print('/\  '*10)
print('  \/'*10)


for x in range(10):
    for y in range(x):
        print(y)


for x in range(1, 10, 3):
    print(x)