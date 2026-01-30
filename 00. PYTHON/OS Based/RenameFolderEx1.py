#Program for Renaming a Folder--we use os.rename()
#Syntax:  os.rename("Old Folder Name  "," New Folder Name ")
#RenameFolderEx1.py
import os
try:
    os.rename("KV","HYD")
    print("Folder Renamed--verify")
except FileNotFoundError:
    print("Folder Name does not Exist")