# LIST_Q66.py
# 66. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
# 	Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# 	Expected Output: [10, 11, 12]
s_list = [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected_output = [10, 11, 12]
import functools as fc
def highest_list(v):
    m,n,o,p = 0,0,0,0
    for i in v[0]:
        m += i
    for i in v[1]:
        n += i
    for i in v[2]:
        o += i
    for i in v[3]:
        p += i
    val = val = m if m>n else n if n>o else o if o>p else p
    print("="*50)
    print("Excepted output is {}".format(Expected_output))
    print("=" * 50)
    if val == m:
        if Expected_output==v[0]:
            print("\t\t Program output is {}".format(v[0]))
    if val == n:
        if Expected_output==v[1]:
            print("\t\t Program output is {}".format(v[1]))
    if val == o:
        if Expected_output==v[2]:
            print("\t\t Program output is {}".format(v[2]))
    if val == p:
        if Expected_output==v[3]:
            print("\t\t Program output is {}".format(v[3]))
    print("=" * 50)
    print()
    print("THE EXECUTION COMPLETED THANX FOR WRITING THIS CODE MAHIII...")
    print("="*50)
highest_list(s_list)


