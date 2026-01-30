#Program for Deciding wether the citizen is eligible to vote or not
#VoterEx2.py
while(True):
    age=int(input("Enter age of Citizen:"))
    if(age>=18) and (age<=100):
        break
    print("\t{} Invalid Age--try Again".format(age))

print("\t{} Years Age Citizen is Eligible to Vote".format(age))