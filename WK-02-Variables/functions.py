# function with single parameter
def greeting(name):
    print("Welcome, "+name)

greeting("John Doe")

# function with multople arguments
def new_greeting(name, department):
    print("Welcome, "+name)
    print("You are part of "+department)

new_greeting("John","Accounting")
new_greeting("Ellis","Software Engineering")

# function with no parameters
def func_no_params():
    """
    docstring
    """
    print("function with no parameters")
    
func_no_params()
    
def area_circle(radius):
    """
    docstring
    """
    print("Area of circle :" +str(3.14 * radius**2))

area_circle(2)

"""
functions with return values
"""
def area_triangle(base,height):
    """
    docstring
    """
    return (base*height)/2
    pass

area_a = area_triangle(7,3)
area_b = area_triangle(5,4)
sum = area_a+area_b
print("Total "+str(sum))


def get_seconds(hours, minutes, seconds):
    return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a + amount_b
print(result)

# function with multiple return values
def convert_seconds(seconds):
    """
    1 hour = 3600 seconds
    l minute = 60 seconds
    """
    hours = seconds//3600
    minutes = (seconds - (hours * 3600))//60
    remaining_seconds = seconds-hours*3600 - minutes *60

    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours,minutes,seconds)


def lucky_number(name):
    """
    docstring
    """
    number = len(name) * 9
    print("Hello "+ name +". Your lucky number is "+str(number))
    pass

lucky_number("Key")
lucky_number("Sudheer")

def month_days(month, days):
    """
    docstring
    """
    print(month + " has " + str(days) + " days.")
    pass

month_days("June",30)
month_days("August",31)



def convert_distance(miles):
    km = miles * 1.6  # approximately 1.6 km in 1 mile
    return km

my_trip_miles = 55

my_trip_km = convert_distance(my_trip_miles)
print("The distance in kilometers is " +str(my_trip_km))
