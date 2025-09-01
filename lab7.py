import numpy as np

# a. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
def a():
    matrix = np.arange(2, 11).reshape(3, 3)
    print("3x3 Matrix:\n", matrix)


# b. Write a NumPy program to reverse an array (the first element becomes the last).
def b():
    arr = np.array([1, 2, 3, 4, 5])
    print("Original:", arr)
    print("Reversed:", arr[::-1])


# c. Write a NumPy program to find common values between two arrays.
def c():
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([4, 5, 6, 7, 8])
    common = np.intersect1d(arr1, arr2)
    print("Common values:", common)


# d. Write a NumPy program to repeat array elements.
def d():
    arr = np.array([1, 2, 3])
    repeated = np.repeat(arr, 3)
    print("Repeated array:", repeated)


# e. Write a NumPy program to find the memory size of a NumPy array.
def e():
    arr = np.array([10, 20, 30, 40, 50])
    print("Memory size (bytes):", arr.nbytes)


# f. Write a NumPy program to create an array of ones and zeros.
def f():
    ones = np.ones((2, 3))
    zeros = np.zeros((2, 3))
    print("Ones array:\n", ones)
    print("Zeros array:\n", zeros)


# g. Write a NumPy program to find the 4th element of a specified array.
def g():
    arr = np.array([10, 20, 30, 40, 50])
    print("4th element:", arr[3])  # index starts from 0
