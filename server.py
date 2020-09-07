import socket
s = socket.socket()
s.bind(('localhost', 1729))
print("server socket created")
s.listen(2)
print("waiting for connections...")
while True:
    c, add = s.accept()
    print("connected with",add)
    c.send(bytes("Welcome To Navodaya", "utf-8"))
    c.close()