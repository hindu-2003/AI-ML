#Program for Demonstrating How to use Local and Global Variables
#LocalGlobalVarEx2.py
def learnAI():
    sub1="AI" # here sub1 is local Variable
    print("To Develop '{}' Based Application, we use '{}' Prog Lang".format(sub1,lang))
def learnML():
    sub2="ML" # here sub2 is local Variable
    print("To Develop '{}' Based Application, we use '{}' Prog Lang".format(sub2,lang))
lang="PYTHON" # Here lang is called Global Variable
def learnDL():
    sub3="DL" # here sub3 is local Variable
    print("To Develop '{}' Based Application, we use '{}' Prog Lang".format(sub3,lang))
#Main Program
learnAI() # Function call
learnML() # Function call
learnDL() # Function call