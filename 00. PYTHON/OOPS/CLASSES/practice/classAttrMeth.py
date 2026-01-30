#classAttrMeth.py
class student:
    """The student require the data
    i love you"""
# Main Program
s1 = student()
print("__doc__")
print(student.__str__)
print("__dict__")
print(s1.__str__)
print("__module__")
print(s1.__module__)
print("__class__")
print(s1.__class__)
print("__dir__")
print(s1.__dir__(),len(s1.__dir__()))
print("__format__")
print(s1.__format__)
print("__getstate__")
print(s1.__getstate__())
print("__hash__")
print(s1.__hash__())
print('__init__')
print(s1.__init__())
print('__repr__')
print(s1.__repr__())
print('__reduce__')
print(s1.__reduce__())

#help(student)
