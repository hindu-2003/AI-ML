print("\tEXCEPTION HANDLING")
print("="*50)
while(" "):
    try:
        s1 = int(input("Enter First Values:"))
        s2 = int(input("Enter Second Values:"))
        c = s1/s2
        print(c)
        break
    except Exception as e :
        print("oops !",repr(e))