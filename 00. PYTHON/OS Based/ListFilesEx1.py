#Program for Listing the Files
#ListFilesEx1.py
import os
filenames=os.listdir("C:\\Users\\KVR\\PycharmProjects\\6PMFiles")
print("------------------------------------------")
print("Number of Files=",len(filenames))
print("------------------------------------------")
for filename in filenames:
    print(filename)
print("------------------------------------------")