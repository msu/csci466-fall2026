import socket

port = 9000
host = socket.gethostname()

print(host)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind((host,port))

serverSocket.listen(1);
connection, addr = serverSocket.accept()

data = connection.recv(1024).decode()

print(data)

connection.send("Got it!!".encode())