#LIST_Q25.py
# Write a Python program to select an item randomly from a list.
while(True):
    import random
    print("Enter Your List for Create a list:")
    items = [val for val in input().split()]
    random_item = random.choice(items)
    print("Randomly selected item:", random_item)
