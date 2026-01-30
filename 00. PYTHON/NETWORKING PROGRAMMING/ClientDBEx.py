#ClientDBEx.py
import socket
s=socket.socket()
s.connect(("127.0.0.1",3600))
empno=input("Enter Employee Number for Getting Other Details:")
s.send(empno.encode())
res=s.recv(1024).decode()
print("-------------------------------------------------")
print(res)
print("-------------------------------------------------")