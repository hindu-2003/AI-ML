#AopDemo.py<---File Name
from AopMenu import AopMenu
from Operations import addop,subop,mulop,divop,expop,modop
import sys
while(True):
    AopMenu()
    ch=int(input("Enter ur Choice:"))
    match(ch):
        case 1:
            addop()
        case 2:
            subop()
        case 3:
            mulop()
        case 4:
            divop()
        case 5:
            modop()
        case 6:
            expop()
        case 7:
            sys.exit()
        case _:
            print("UR Selection of Operation wrong-try again")
