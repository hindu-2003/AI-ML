#Program for Obtaining List of  Digits from Given Line of Alhanumerical Values
#FilterFunsEx6.py
line=input("Enter Line of Text:") # P3yth6on is a7n oo9p l8ang
digs=list(filter(lambda ch: ch.isdigit(),line))
print("Digits Found")
print(",".join(digs))