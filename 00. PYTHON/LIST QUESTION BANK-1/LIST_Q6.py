 #Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
	# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
	# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
Given_list=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected_Result=[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
lst = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sl = []
fl = []
Expected = []
for i in lst:
    sl.append(list(i)[::-1])
sl.reverse()
sl.sort()
for j in sl:
    fl.append(j[::-1])
for k in fl:
    Expected.append(tuple(k))
print("\t","_"*65)
print("\t\tGiven   List: {}".format(lst))
print("\t","~"*65)
print("\t\tExpected Result: {}".format(Expected))
print("\t","*"*65)

if Expected_Result==Expected:
    print("\t\t\t\tPROGRAM EXECUTE PERFECTLY")
else:
    ("\t\tPLEASE TRY AGAIN --NOT MATCHED THE RESULT")




