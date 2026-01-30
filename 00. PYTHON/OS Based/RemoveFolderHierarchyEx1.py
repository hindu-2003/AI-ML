#Proggram for Removing a Folders Hierarchy---we use os.removedirs()
#RemoveFolderHierarchyEx1.py
import os
try:
    os.removedirs("C:\\India\\HYD\\PYTHON\\kvr")
    print("Folders Hierarchy Removed--verify")
except FileNotFoundError:
    print("Folders Hierarchy does not exist")