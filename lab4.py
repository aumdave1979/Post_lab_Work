# a. Write a Python program to multiply all the items in a list.
def a():
    numbers = [2, 3, 4, 5]   # sample list
    result = 1
    for num in numbers:
        result *= num
    print("Product of all items:", result)


# b. Write a Python program to get the largest number from a list.
def b():
    numbers = [10, 25, 67, 34, 89, 12]
    print("Largest number:", max(numbers))


# c. Write a Python program to remove duplicates from a list.
def c():
    items = ["apple", "banana", "apple", "orange", "banana", "grape"]
    unique_items = list(set(items))
    print("List after removing duplicates:", unique_items)


# d. Write a Python program to get the frequency of elements in a list.
def d():
    items = ["cat", "dog", "cat", "bird", "dog", "dog", "fish"]
    frequency = {}
    for item in items:
        frequency[item] = frequency.get(item, 0) + 1
    print("Frequency of elements:", frequency)


# e. Find common items from two lists.
def e():
    list1 = ["red", "blue", "green", "yellow"]
    list2 = ["green", "yellow", "black", "white"]
    common = list(set(list1) & set(list2))
    print("Common items:", common)


# f. Convert a list of multiple integers into a single integer.
def f():
    numbers = [1, 2, 3, 4, 5]
    single_integer = int("".join(map(str, numbers)))
    print("Single integer:", single_integer)
