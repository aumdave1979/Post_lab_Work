# Write a python code for calculating the Area and Perimeter of a Rectangle

def a(): 
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    area = length * width
    perimeter = 2 * (length + width)
    print("Area of the rectangle:", area)
    print("Perimeter of the rectangle:", perimeter)

# Write a python code for testing if a number is even or odd

def b():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(num, "is Even")  
    else:   
        print(num, "is Odd")

# Write a python code for calculate the area and volume of the Cube.

def c():
    side = float(input("Enter the side length of the cube: "))
    surface_area = 6 * (side ** 2)
    volume = side ** 3
    print("Surface Area of the cube:", surface_area)
    print("Volume of the cube:", volume)

# Write a python code to solve the equation z = (x+y)*(x-y)
def d():
    x = float(input("Enter value of x: "))
    y = float(input("Enter value of y: "))
    z = (x + y) * (x - y)
    print("Value of z =", z)

# Write a python code to solve the equation z = (x+y)*(x+y)-2xy; write a comment on it.

def e():
    x = float(input("Enter value of x: "))
    y = float(input("Enter value of y: "))
    z = (x + y) * (x + y) - 2 * x * y   
    print("Value of z =", z)

# Write a python code for Converting Celsius to Fahrenhit

def f():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)





