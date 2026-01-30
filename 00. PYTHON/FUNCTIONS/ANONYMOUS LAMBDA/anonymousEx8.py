#write a program for checking palindrome or not with anonymous functions
#anonymousEx8.py
palindrome=lambda word: "palindrome" if word==word[::-1] else "Not Palindrome"
#main program
word=input("Enter a word it check for palindrome or not:")
res = palindrome(word)
print("*"*50)
print(" \t\t  \t{} is {}".format(word,res))
print("*"*50)