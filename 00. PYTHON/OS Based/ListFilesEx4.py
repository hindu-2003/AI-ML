#Program for Listing the Files whose extension is .py
#ListFilesEx4.py
import os
filenames=os.listdir("C:\\Users\\KVR\\PycharmProjects\\6PMFiles")
print("------------------------------------------")
print("Number of Files=",len(filenames))
print("------------------------------------------")
for filename in filenames:
    if(filename.startswith("File")):
        print(filename)
print("------------------------------------------")
