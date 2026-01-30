#StudentMarksReportEx1.py
#validation of student number
while(True):
    sno=int(input("Enter Student Number:"))
    if(sno>0):
        break
    print("\t{} is Invalid Student Number".format(sno))

#Validation of name
while(True):
    urname=input("Enter Ur Name:") # urname=Guido Van Ro4ssum
    if(len(urname)==0):
        print("\tDon't enter space for Name--try again")
    else:
        #validation Code for name
        words=urname.split()  # ['Guido', 'Va$n', 'Ro4ssum']
        res="valid"
        for word in words:
            if( not word.isalpha()):
                res="invalid"
                break
        if(res=="invalid"):
            print("{} is Invalid Name--try again".format(urname))
        elif(res=="valid"):
            break
#Validation of CM
while(True):
    cm=int(input("Enter Marks in C:"))
    if(0<=cm<=100):
        break
    print("\t{} Marks in C invalid".format(cm))
#Validation of CPPM
while(True):
    cppm=int(input("Enter Marks in CPP:"))
    if(cppm in range(0,101)):
        break
    print("\t{} Marks in CPP invalid".format(cppm))
#Validation of OSM
while(True):
    osm=int(input("Enter Marks in OS:"))
    if(osm in range(0,101)):
        break
    print("\t{} Marks in OS invalid".format(osm))
# Calculate totmarks (totmarks=CM+CPPM+OSM)
totmarks=cm+cppm+osm
#Calculate percent of marks (percent= (totmarks/300)*100) )
percent=round((totmarks/300)*100,2)
#if student secure less than 40 in any one of the subject then give grade="FAIL"
if(cm<40) or  (cppm<40) or  (osm<40):
    grade="FAIL"
else:
    #if totmarks ranges between 250 and 300 then give grade="DISTINCTION"
    if(totmarks<=300) and (totmarks>=250):
        grade="DISTINCTION"
    elif(250>totmarks>=200):
        grade="FIRST"
    elif(totmarks in range(150,200)):
        grade="SECOND"
    elif(totmarks in range(120, 150)):
        grade="THIRD"
# Display the Student Marks Report
print("="*50)
print("\t\tSTUDENT MARKS REPORT")
print("="*50)
print("\t\tStudent Number:{}".format(sno))
print("\t\tStudent Name:{}".format(urname))
print("\t\tStudent Marks in C:{}".format(cm))
print("\t\tStudent Marks in C++:{}".format(cppm))
print("\t\tStudent Marks in OS:{}".format(osm))
print("-"*50)
print("\t\tStudent Total Marks :{}".format(totmarks))
print("\t\tStudent Percentage of Marks :{}".format(percent))
print("\t\tStudent Grade :{}".format(grade))
print("="*50)
