import pandas as pd
def a():
    # Sample data
    series1 = pd.Series([2, 4, 6, 8, 10])
    series2 = pd.Series([1, 3, 5, 7, 9])

    # Addition
    addition = series1 + series2
    print("Addition:")
    print(addition)

    # Subtraction
    subtraction = series1 - series2
    print("\nSubtraction:")
    print(subtraction)

    # Multiplication
    multiplication = series1 * series2
    print("\nMultiplication:")
    print(multiplication)

    # Division
    division = series1 / series2
    print("\nDivision:")
    print(division)

def b():

    # Sample dictionary
    data = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}
    # Convert the dictionary to a Pandas Series
    series = pd.Series(data)
    # Print the resulting Series
    print(series)

def c():
    # Create a list
    my_list = [10, 20, 30, 40, 50]

    # Convert the list to a Series
    series_from_list = pd.Series(my_list)

    print("Series from a list:")
    print(series_from_list)

def d():

    # Create a dictionary
    my_dict = {'a': 100, 'b': 200, 'c': 300}

    # Convert the dictionary to a Series
    series_from_dict = pd.Series(my_dict)

    print("\nSeries from a dictionary:")
    print(series_from_dict)

d()