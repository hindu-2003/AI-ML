#  LIST_Q65.py
# 65. Write a Python program to move all zero digits to end of a given list of numbers.
# 	Expected output:
# 	Original list:
org = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# 	Move all zero digits to end of the said list of numbers:
eo = [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
eo1 = []
eo2 = []
for i in org:
    if i != 0:
        eo1.append(i)
for j in org:
    if j == 0:
        eo2.append(j)
fo = eo1+eo2
print(fo)

