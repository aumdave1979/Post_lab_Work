# a. Write a Python program to Count the occurrences of an element in a tuple.
def a():
    tup = (1, 2, 3, 2, 4, 2, 5)
    element = 2
    count = tup.count(element)
    print(f"Occurrences of {element}:", count)


# b. Write a Python program to Check if an element exists in a tuple.
def b():
    tup = ("apple", "banana", "cherry")
    element = "banana"
    if element in tup:
        print(f"{element} exists in the tuple")
    else:
        print(f"{element} does not exist in the tuple")


# c. Write a Python program to Convert a tuple to a string.
def c():
    tup = ("H", "e", "l", "l", "o")
    string = "".join(tup)
    print("Converted string:", string)


# d. Write a Python program to Find the maximum and minimum elements in a tuple.
def d():
    tup = (10, 25, 4, 67, 89, 12)
    print("Maximum element:", max(tup))
    print("Minimum element:", min(tup))


# e. Write a Python program to convert a tuple of strings to a single string.
def e():
    tup = ("Python", "is", "fun")
    string = " ".join(tup)
    print("Single string:", string)


# f. Write a Python program to sort a tuple of integers.
def f():
    tup = (5, 2, 9, 1, 7)
    sorted_tuple = tuple(sorted(tup))
    print("Sorted tuple:", sorted_tuple)


# g. Write a python program to find the first and last elements of a tuple.
def g():
    tup = (10, 20, 30, 40, 50)
    print("First element:", tup[0])
    print("Last element:", tup[-1])
