#program for Dynamic create file
print("Enter the Text for Dynamic and stop for press @ :")
while(1):
    with open("Python","a") as p:
        kbinput = input()
        if kbinput!="@":
            p.write(kbinput+"\n")
        else:
            print("Writing completed ---verify")
            break
