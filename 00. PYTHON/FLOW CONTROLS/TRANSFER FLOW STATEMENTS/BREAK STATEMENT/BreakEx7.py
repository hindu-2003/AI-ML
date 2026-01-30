#Program for deciding wether the given word is vowel word or not
#BreakEx7.py
import sys
s=input("Enter Any word:")
found="Not Vowel Word"
for ch in s:
    if ch.lower() in ['a','e','i','o','u']:
        found="Vowel Word"
        break
print("{} is {}".format(s,found))
