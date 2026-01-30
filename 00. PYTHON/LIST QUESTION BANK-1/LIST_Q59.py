##LIST_Q59.py
#Write a Python program to check whether the n-th element exists in a given list.
def nth(lst, n):
    if n < len(lst):
        print("The {}th element: {}".format(n,lst[n]))
    else:
        print("The {}th element does not exist in the list.".format(n))
list = [int(val) for val in input("Enter for list with spaces: ").split()]
n = int(input("Enter for which position :"))
print(list)
nth(list, n)



