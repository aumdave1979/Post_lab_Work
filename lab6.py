# a. Write a Python program to print all odd numbers between 1 to 100 using a while loop.
def a():
    i = 1
    while i <= 100:
        if i % 2 != 0:
            print(i, end=" ")
        i += 1
    print()


# b. Write a Python program to find the sum of all natural numbers between 1 to n.
def b():
    n = 10  # sample
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    print("Sum of natural numbers from 1 to", n, "=", total)


# c. Write a Python function program to count a number of digits in a number.
def c():
    num = 123456
    count = 0
    while num > 0:
        num //= 10
        count += 1
    print("Number of digits:", count)


# d. Write a Python program to find the first and last digits of a number.
def d():
    num = 98765
    last = num % 10
    first = num
    while first >= 10:
        first //= 10
    print("First digit:", first)
    print("Last digit:", last)


# e. Write a Python program to swap the first and last digits of a number.
def e():
    num = 12345
    num_str = str(num)
    if len(num_str) > 1:
        swapped = num_str[-1] + num_str[1:-1] + num_str[0]
    else:
        swapped = num_str
    print("Number after swapping:", swapped)


# f. Write a Python program to calculate the product of digits of a number.
def f():
    num = 2345
    product = 1
    for digit in str(num):
        product *= int(digit)
    print("Product of digits:", product)


# g. Write a Python program to enter a number and print its reverse.
def g():
    num = 12345
    reverse = str(num)[::-1]
    print("Reverse of number:", reverse)
