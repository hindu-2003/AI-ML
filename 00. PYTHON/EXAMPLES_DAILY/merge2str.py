#Program for merge characters of  2 strings into a single string by taking characters alternatevely
s1 = input("Enter the first name:") #rama
s2 = input("Enter the second name:") #sita
op = ''
i = 0
j = 0

while i<len(s1):
    op = op+s1[i]
    i = i+1
    if j<len(s2):
        op = op + s2[j]
        j = j+1
print(op)

