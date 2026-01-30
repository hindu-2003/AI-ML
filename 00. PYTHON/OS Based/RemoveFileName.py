#Program for Removing the File Name---we use remove()
#Syntax: os.remove(File Name)
#RemoveFileName.py
import os
try:
    os.remove("kvr2.data")
    print("File Removed--verify")
except FileNotFoundError:
    print("File does not exist")