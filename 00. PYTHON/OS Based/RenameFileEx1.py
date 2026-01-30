#Program for Renaming a File--we use os.rename()
#Syntax:  os.rename("Old File Name  ","New File Name")
#RenameFileEx1.py
import os
try:
    os.rename("pyt.png","kvr.png")
    print("File name Renamed--verify")
except FileNotFoundError:
    print("File Name does not Exist")