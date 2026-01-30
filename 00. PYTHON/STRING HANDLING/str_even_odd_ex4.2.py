n = input("Enter a string:") #ramu
i = 0
print("Characters at even position")
while i<len(n):
    print(n[i])
    i = i+2


print("Characters at odd position")
i = 1
while i<len(n):
    print(n[i],end=',')
    i=i+2


