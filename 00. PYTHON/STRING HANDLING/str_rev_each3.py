#write a program to print characters at odd positions and even position for the given string.
s = input("Enter the sentence:")
l = (s.split())[::-1]
l1 = []
i = 0
while i<len(l):
    l1.append(l[i][::-1])
    i = i+1
    x = ' '.join(l1)
print(x)



