print("\tEXCEPTION HANDLING")
print("="*50)
while(" "):
    try:
        s1 = int(input("Enter First Values:"))
        s2 = int(input("Enter Second Values:"))
        c = s1/s2
        print(c)
        break
    except ValueError:
        print("\tDon't Enter Alpha-nums,symbols--try again")
    except ZeroDivisionError:
        print("\t Don't Enter zero to the  Denominator")
