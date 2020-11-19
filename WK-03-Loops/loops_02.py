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
