#Program for Demonstrating continue statement
#ContinueStmtEx2.py
s="PYTHON"
i=0
while(i<len(s)):
    print(s[i])
    i=i+1
else:
    print("while..else part")
print("----------------------------------")
#I want to display  PTON
i=0
while(i<len(s)):
    if(s[i]=="H") or (s[i]=="Y"):
        i = i + 1
        continue
    print(s[i])
    i=i+1
else:
    print("while..else part")