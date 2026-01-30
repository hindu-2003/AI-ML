#Program for Demonstrating How to use Local and Global Variables
#LocalGlobalVarEx1.py
def learnAI():
    sub1="AI" # here sub1 is local Variable
    print("To Develop '{}' Based Application, we use '{}' Prog Lang".format(sub1,lang))
    #print(sub2,sub3)---we can't access sub2 and sub3 bcoz they are local in other funs
def learnML():
    sub2="ML" # here sub2 is local Variable
    print("To Develop '{}' Based Application, we use '{}' Prog Lang".format(sub2,lang))
    # print(sub1,sub3)---we can't access sub1 and sub3 bcoz they are local in other funs
def learnDL():
    sub3="DL" # here sub3 is local Variable
    print("To Develop '{}' Based Application, we use '{}' Prog Lang".format(sub3,lang))
    # print(sub1,sub2)---we can't access sub1 and sub2 bcoz they are local in other funs
#Main Program
lang="PYTHON" # Here lang is called Global Variable
learnAI() # Function call
learnML() # Function call
learnDL() # Function call