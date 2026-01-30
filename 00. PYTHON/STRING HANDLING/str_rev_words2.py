s = input("Enter a sentence:")
l=s.split()
l1 = []
i = len(l)-1
while i>=0:
    l1.append(l[i])
    i-=1
print(l)
print(l1)
