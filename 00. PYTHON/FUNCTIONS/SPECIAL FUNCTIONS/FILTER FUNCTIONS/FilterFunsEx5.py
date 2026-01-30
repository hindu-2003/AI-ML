#Program for Obtaining List of  words  whose length range from 3 or 4 from List of words
#FilterFunsEx5.py
print("Enter List of Values Separated by Comma:")
words=[word for word in input().split(",")]
print("Given Words=",words)
#Get the words whose length lies within 3 and 4
words34=list(filter(lambda word:word.isalpha() and 3<=len(word)<=4,words))
print("List of words with length 3 or 4")
print(words34)