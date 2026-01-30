#Program for Demonstrating How to use Local and Global Variables
#LocalGlobalVarEx3.py
def learnAI():
    sub1="AI" # here sub1 is local Variable
    print("To Develop '{}' Based Application, we use '{}' Prog Lang".format(sub1,lang))
def learnML():
    sub2="ML" # here sub2 is local Variable
    print("To Develop '{}' Based Application, we use '{}' Prog Lang".format(sub2,lang))
def learnDL():
    sub3="DL" # here sub3 is local Variable
    print("To Develop '{}' Based Application, we use '{}' Prog Lang".format(sub3,lang))
#Main Program
#learnAI() # Function call--In this function we can't access 'lang' global var bcoz It is defined after function call
lang="PYTHON" # Here lang is called Global Variable
learnML() # Function call
learnDL() # Function call
