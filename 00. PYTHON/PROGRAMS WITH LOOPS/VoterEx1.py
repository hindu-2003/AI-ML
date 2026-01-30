#Program for Deciding wether the citizen is eligible to vote or not
#VoterEx1.py
age=int(input("Enter age of Citizen:"))
if(age>=18):
    print("{} Years Age Citizen is Eligible to Vote".format(age))
else:
    print("{} Years Age Citizen is Not Eligible to Vote".format(age))
