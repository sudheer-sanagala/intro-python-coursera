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