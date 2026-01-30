#MatchCaseEx4.py
wkd=input("Enter Week Name:").upper()
match(wkd):
    case "MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY":
        print("{} is Working Day".format(wkd))
    case "SATURDAY":
        print("{} is Weekd END".format(wkd))
    case "SUNDAY":
        print("{} is Holi Day".format(wkd))
    case _:
        print("{} is not a week day--try again".format(wkd))

