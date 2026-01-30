#Program for Obtaining List of Palindrome words from List of Values
#FilterFunsEx4.py
print("Enter List of Words separated by Space:")
words=[word for word in input().split()]
print("Given Words=",words)
#Get Palindrome List
palwords=list(filter(lambda word: word==word[::-1],words))
print("List of Palindrome Words=",palwords)