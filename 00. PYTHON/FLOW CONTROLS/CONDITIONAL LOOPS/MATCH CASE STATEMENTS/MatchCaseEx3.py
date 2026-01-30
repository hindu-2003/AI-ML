#MatchCaseEx3.py
wkd=input("Enter Week Name:")
match(wkd):
    case "MONDAY":
        print("{} is Working Day".format(wkd))
    case "TUESDAY":
        print("{} is Working Day".format(wkd))
    case "WEDNESDAY":
        print("{} is Working Day".format(wkd))
    case "THURSDAY":
        print("{} is Working Day".format(wkd))
    case "FRIDAY":
        print("{} is Working Day".format(wkd))
    case "SATURDAY":
        print("{} is Weekd END".format(wkd))
    case "SUNDAY":
        print("{} is Holi Day".format(wkd))
    case _:
        print("{} is not a week day--try again".format(wkd))

