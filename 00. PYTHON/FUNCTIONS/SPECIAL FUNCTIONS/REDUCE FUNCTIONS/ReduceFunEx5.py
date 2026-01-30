#Program for Accepting list of Values and concat them by using reduce()
#ReduceFunEx5.py
import functools
def concatop(k,v):
    return (k+" "+v)
#Main Program
print("Enter List of words separated by Comma:")
words=[word for word in input().split(",")]
print("Given Words")
print(words)
#Code for concatenating Words which are present in list
line=functools.reduce(concatop,words)
print(line)