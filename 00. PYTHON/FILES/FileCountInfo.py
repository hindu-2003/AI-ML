#Program for Counting Number of Lines, words and chars of any file
#FileCountInfo.py
def filecountinfo():
    try:
        filename=input("Enter Any File Name:")
        with open(filename,"rt") as fp:
            nol=0
            now=0
            noc=0
            lines=fp.readlines()
            for line in lines:
                nol+=1
                now=now+len(line.split())
                noc=noc+len(line)
            else:
                print("----------------------")
                print("Number of Lines=",nol)
                print("Number of Words=",now)
                print("Number of Chars=",noc)
                print("----------------------")
    except FileNotFoundError:
        print("File Does not Exist")
#Main Program
filecountinfo()