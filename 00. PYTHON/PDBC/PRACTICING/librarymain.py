import oracledb
from librarymenu import menu
from libraryadd import addbook
from librarydelete import deletebook
from libraryupdate import updatebook
from libraryview import viewbook,viewallbooks
def main():
    while(True):
        menu()
        ch = int(input("Enter Your choice : "))
        match(ch):
            case 1:
                addbook()
            case 2:
                deletebook()
            case 3:
                updatebook()
            case 4:
                viewbook()
            case 5:
                viewallbooks()
            case 6:
                print("Thanks for using this program")
                break

main()
