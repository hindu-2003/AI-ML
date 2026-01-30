#Program reading a Line of Text and display other than Vowels
#ContinueStmtEx3.py
line=input("Enter a Line of Text:")
print("Given Line:{}".format(line)) # Apple
print("-----------------------------")
for ch in line:
    if ch.lower() in ["a","e","i","o","u"] :
        continue
    else:
        print(ch,end="")
