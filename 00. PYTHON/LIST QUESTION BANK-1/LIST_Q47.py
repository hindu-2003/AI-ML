# Write a Python program to insert an element before each element of a list
#LIST_Q47.PY
# lst1 = [10,30,50,70,90]
class mahesh:
    @staticmethod
    def blist(lst):
        l = []
        for i in lst:
            a = i[0], i
            l.append(a)
        print(l)

# Main program
lst = [(val) for val in input("Enter the  values for list :").split() ]
m = mahesh()
m.blist(lst)

