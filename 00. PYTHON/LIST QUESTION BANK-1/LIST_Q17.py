#LIST_Q17.py
#Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included)
squares = [i**2 for i in range(1, 31)]
print("---"*17)
print("list of squares of Numbers Except first five numbers")
print("-"*50)
print("First 5 elements:\n", squares[4:])
print("* "*25)
