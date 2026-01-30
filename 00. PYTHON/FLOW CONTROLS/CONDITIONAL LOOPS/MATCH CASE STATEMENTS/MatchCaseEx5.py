#MatchCaseEx5.py
wkd=input("Enter Week Name:").strip()
if wkd.upper() in ["MONDAY","TUESDAY","WEDNESDAY","THURDAY","FRIDAY","SATURDAY","SUNDAY","MON","TUE","WED","THU","FRI","SAT","SUN"]:
    match(wkd.upper()):
        case "MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURDAY"|"FRIDAY"|"MON"|"TUE"|"WED"|"THU"|"FRI":
            print("{} is Working Day".format(wkd))
        case "SATURDAY"|"SAT":
            print("{} is Weekd END".format(wkd))
        case "SUNDAY"|"SUN":
            print("{} is Holi Day".format(wkd))
else:
    print("{} is not a week day".format(wkd))



