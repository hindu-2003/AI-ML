#Program accepting a word or value and decide whether a word or value is palindrome or not
value=input("Enter Value:")
res="Palindrome" if value==value[::-1] else "Not Palindrome"
print("{} is {}".format(value,res))