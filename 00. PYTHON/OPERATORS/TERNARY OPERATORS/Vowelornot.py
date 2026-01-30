#Program for deciding whether the Word is Vowel or not
#Vowelornot.py
word=input("Enter a word:")
res="Vowel Word" if "a" in word or "e" in word or "i" in word or "o" in word or "u" in word or "A" in word or "E" in word or "I" in word or "O" in word or "U" in word else "Not Vowel Word"
print("{} is {}".format(word,res))