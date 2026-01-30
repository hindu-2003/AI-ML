#Program for creating a Folders Hierarchy--os.makedirs()
#Syntax: os.makedirs("Folders Hierarchy")
#CreateFoldersHierarchyEx1.py
import os
try:
    os.makedirs("C:\\India\\HYD\\PYTHON\\kvr")
    print("Folders Hierarchy Created--verify")
except FileExistsError:
    print("Folders Hierarchy already Exist")