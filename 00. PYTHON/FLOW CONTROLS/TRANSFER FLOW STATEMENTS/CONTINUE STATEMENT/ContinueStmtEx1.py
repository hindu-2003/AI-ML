#Program for Demonstrating continue statement
#ContinueStmtEx1.py
s="PYTHON"
for ch in s:
    print(ch)
else:
    print("for loop---else part")
print("-----------------------------------------")
#I want to display  PYHON
for ch in s:
    if(ch=="T"):
        continue
    else:
        print(ch)
else:
    print("for loop---else part")

