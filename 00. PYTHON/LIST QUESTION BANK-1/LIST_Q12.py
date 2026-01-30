# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#LIST_Q12.py
def remove_elements(a):
    return [element for i, element in enumerate(a) if i not in [0, 4, 5]]

# Test the function
list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(remove_elements(list))  # Output: ['Green', 'White', 'Black']

