#Program for creating a Create a Folder---we use mkdir()
#Syntax:  os.mkdir("Folder Name")
#CreateFolderEx1.py
import os
try:
    os.mkdir("KVR")
    print("Folder Created--verify")
except FileExistsError:
    print("Folder already created")
except FileNotFoundError:
    print("Plz ensure there must exist Root Folder")