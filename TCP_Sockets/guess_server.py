
import socket
import random

port = 9000
host = socket.gethostname()

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind( (host, port) )

serverSocket.listen(1)

connection, addr = serverSocket.accept()

random_number = random.randint(1,20)

while(True):

    user_guess = int(connection.recv(1024).decode())

    print("User guessed", user_guess)

    if(user_guess > random_number):
        connection.send("Lower".encode())

    elif(user_guess < random_number):
        connection.send("Higher".encode())

    else:
        connection.send("Win!!! You got it".encode())
        break