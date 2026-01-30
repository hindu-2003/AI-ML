#LIST_Q18.py
#Write a Python program to generate all permutations of a list in Python
def permutation(lst):
    for i in lst:
        for j in range(i,j):
            print(i*j)
#main program
lst=[val for val in input().split()]
permutation(lst)