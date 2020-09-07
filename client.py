import socket
c = socket.socket()
c.connect(('localhost',1729))
msg=c.recv(1024)
print(msg.decode("utf-8"))