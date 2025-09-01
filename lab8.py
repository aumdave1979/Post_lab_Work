import math

# a. Write a Python program to convert degree to radian
def a():
    degree = 180   # example value
    radian = math.radians(degree)
    print("a) Degree to Radian:")
    print(f"{degree} degrees = {radian} radians\n")

# b. Make a simplest possible Python program that calculates and prints the value of the formula
#    y = 6x^2 + 4sin(x)
def b():
    x = math.pi / 4   # example value
    y = 6 * (x ** 2) + 4 * math.sin(x)
    print("b) Formula Calculation (y = 6x^2 + 4sin(x)):")
    print(f"For x = {x}, y = {y}\n")


# c. Write a Python function that evaluates the mathematical functions:
#    f(x) = cos(2x), f'(x) = -2sin(2x), f''(x) = -4cos(2x)
#    Return these values for x = pi
def c():
    x = math.pi
    f = math.cos(2 * x)
    f1 = -2 * math.sin(2 * x)
    f2 = -4 * math.cos(2 * x)
    print("c) Function Evaluations for x = pi:")
    print(f"f(x)  = {f}")
    print(f"f'(x) = {f1}")
    print(f"f''(x)= {f2}\n")
