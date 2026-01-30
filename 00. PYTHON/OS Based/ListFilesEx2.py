#Program for Listing the Files whose extension is .py
#ListFilesEx2.py
import os
filenames=os.listdir("C:\\Users\\KVR\\PycharmProjects\\6PMFiles")
print("------------------------------------------")
print("Number of Files=",len(filenames))
print("------------------------------------------")
nop=0
for filename in filenames:
    if(filename.endswith(".py")):
        print(filename)
        nop+=1
print("------------------------------------------")
print("Number of Python Files=",nop)
print("------------------------------------------")