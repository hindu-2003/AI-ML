#Proggram for Removing a Folder---we use os.rmdir()
#Syntax:  os.rmdir("Folder Name")
#RemoveFolderEx1.py
import os
try:
    os.rmdir("KVR")
    print("Folder Removed--verify")
except FileNotFoundError:
    print("Folder does not Exist")
except OSError:
    print("Ensure the Folder must be empty")
