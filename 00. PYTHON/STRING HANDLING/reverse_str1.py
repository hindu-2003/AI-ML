#Write a program to reverse the given string.
#3 ways are string reverse format
#1st way:
s = input("Enter the string:")
#print(s[::-1])

#2nd way
#s = input("Enter the string:")
#M =("".join(reversed(s)))
#print(M,id(M),id(s))
i = len(s)-1
x = ""
while i>=0:
    x = x+s[i]
    i=i-1
print(x)
