#LIST_Q44.py
# Write a Python program to generate groups of five consecutive numbers in a list
print("===========x===========")
numbers = list(range(1, 21))
for i in range(0, len(numbers),5):
    print(numbers[i:i+5])
print("===========x===========")
n = list(range(0,6))
print([n[i:i+3] for i in range(0,len(n),3)])
print("===========x===========")