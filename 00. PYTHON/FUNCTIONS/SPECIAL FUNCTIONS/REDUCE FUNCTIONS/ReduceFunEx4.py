#Program for Accepting list of Values and concat them by using reduce()
#ReduceFunEx4.py
import functools
print("Enter List of words separated by Comma:")
words=[word for word in input().split(",")]
print("Given Words")
print(words)
#Code for concatenating Words which are present in list
line=functools.reduce(lambda k,v:k+" "+v,words)
print(line)