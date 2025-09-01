# a. Write a Python program to reverse a string.
def a():
    s = input("Enter a string to reverse: ")
    print("Reversed string:", s[::-1])


# b. Write a Python program to check if a string is a palindrome.
def b():
    s = input("\nEnter a string to check palindrome: ")
    if s == s[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")


# c. Write a Python program to check if a string contains only digits.
def c():
    s = input("\nEnter a string to check digits only: ")
    if s.isdigit():
        print("The string contains only digits.")
    else:
        print("The string does not contain only digits.")


# d. Write a Python program to find the longest word in a sentence.
def d():
    sentence = input("\nEnter a sentence to find the longest word: ")
    words = sentence.split()
    longest = max(words, key=len) if words else ""
    print("Longest word:", longest)


# e. Write a Python program to find the length of the last word in a sentence.
def e():
    sentence = input("\nEnter a sentence to find length of last word: ")
    words = sentence.strip().split()
    print("Length of last word:", len(words[-1]) if words else 0)
