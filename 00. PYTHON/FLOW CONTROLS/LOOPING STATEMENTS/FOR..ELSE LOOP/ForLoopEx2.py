#ForLoopEx2.py
lst=[10,"Rossum",34.56,True,2+3j,"PYTHON"]
print("By using while loop by using +Ve Indexing")
i=0
while(i<len(lst)):
    print(lst[i])
    i+=1
else:
    print("while--else Part")
print("----------------------------------")
print("By using while loop by using -Ve Indexing")
i=-len(lst)
while(i<=-1):
    print(lst[i])
    i=i+1
print("----------------------------------")
print("By using for loop ")
for ch in lst:
    print(ch)
print("----------------------------------")
print("By using for loop with +ve Index ")
for i in range(0,len(lst)):
    print(lst[i])
print("----------------------------------")
print("By using for loop with -ve Index ")
for i in range(-len(lst),0):
    print(lst[i])
print("----------------------------------")
print("By using for loop with -ve Index in reverse order with Slicing ")
for i in lst[::-1]:
    print(i)
print("----------------------------------")
print("By using for loop with -ve Index in reverse order without slicing ")
for i in range(-1,-len(lst)-1,-1):
    print(lst[i])
else:
    print("=================")